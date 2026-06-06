import sys
import subprocess
import tempfile
import pathlib
import shlex
import uuid


def call_cli_with_input(input_path: str, style: str, max_chunks: int, focus: str):
    script = pathlib.Path(__file__).resolve().parents[1] / 'app.py'
    outf = pathlib.Path(tempfile.gettempdir()) / f'summary_out_{pathlib.Path(input_path).stem}.md'
    cmd = [sys.executable, str(script), '--input', str(input_path), '--style', style, '--max-chunks', str(max_chunks), '--output', str(outf)]
    if focus:
        cmd += ['--focus', focus]
    print('Running:', ' '.join(shlex.quote(p) for p in cmd))
    print('Working... please wait.')
    subprocess.run(cmd, check=True)
    if outf.exists():
        print('\n=== Summary output (preview) ===\n')
        print(outf.read_text(encoding='utf-8'))
        print('\n(Full file saved at: {})'.format(outf))
    else:
        print('No output file produced. Check the CLI logs above for errors.')


def run_repl():
    print('Interactive summarizer REPL')
    print('You can provide a PDF/TXT file path or paste text to summarize.')
    while True:
        print('\nChoose an action:')
        print('  1) Summarize a file (PDF/TXT)')
        print('  2) Paste text to summarize')
        print('  3) Exit')
        choice = input('> ').strip()
        if choice == '1':
            path = input('Enter file path: ').strip('"')
            if not pathlib.Path(path).exists():
                print('File not found:', path)
                continue
            style = input('Output style (concise/detailed) [concise]: ').strip() or 'concise'
            max_chunks = input('Max chunks (4/6/8) [4]: ').strip() or '4'
            focus = input('Optional focus (press Enter to skip): ').strip()
            try:
                call_cli_with_input(path, style, int(max_chunks), focus)
            except Exception as e:
                print('Error calling summarizer:', e)
        elif choice == '2':
            print('Paste the document text below. Do not include the instruction in the pasted text.')
            print('End with a single line containing only "<END>"')
            lines = []
            while True:
                l = input()
                if l.strip() == '<END>':
                    break
                lines.append(l)
            if not lines:
                print('No text entered.')
                continue
            style = input('Output style (concise/detailed) [concise]: ').strip() or 'concise'
            max_chunks = input('Max chunks (4/6/8) [4]: ').strip() or '4'
            focus = input('Optional focus as a short phrase (e.g. methods, results, main contributions): ').strip()
            tmp = pathlib.Path(tempfile.gettempdir()) / f'interactive_input_{uuid.uuid4().hex}.txt'
            tmp.write_text('\n'.join(lines), encoding='utf-8')
            try:
                call_cli_with_input(str(tmp), style, int(max_chunks), focus)
            except Exception as e:
                print('Error calling summarizer:', e)
        elif choice == '3' or choice.lower() in ('q', 'quit', 'exit'):
            print('Exiting.')
            break
        else:
            print('Invalid choice')


if __name__ == '__main__':
    run_repl()
