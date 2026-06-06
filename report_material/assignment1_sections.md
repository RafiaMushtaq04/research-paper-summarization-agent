# Assignment-1 Proposal and Literature Survey

## 1. Project Selection
Selected Domain: Research and Academic Assistance  
Selected Sub-topic: Research Paper Summarization Agent

## 2. Project Goal
The objective of this project is to design and develop an AI-based research paper summarizer that can automatically generate concise and meaningful summaries from lengthy academic documents. With the rapid growth of scientific publications, researchers and students often face difficulty in quickly extracting relevant information from large volumes of text. This project addresses that challenge by providing an intelligent solution that reduces reading time while preserving key insights.

The problem this agent will solve is the inefficiency and time consumption associated with manually reading and understanding research papers. Academic papers are often lengthy, complex, and filled with technical details, making it difficult for users to identify the main contributions and findings quickly. The proposed AI agent processes these documents and extracts or generates summaries that highlight the most important information.

The target users of this system include students, researchers, educators, and professionals who frequently engage with academic literature. It can be applied in domains such as education, scientific research, and knowledge management, where quick comprehension of research content is essential.

The AI agent performs tasks such as analyzing paper text, identifying key sections and important sentences, and generating a coherent summary. Depending on the query and context, the system may apply extractive behavior (information selection) and abstractive behavior (human-like rewriting) to improve accuracy, relevance, and readability. Unlike a generic short-text summarizer, the proposed work is designed for long scientific documents and returns structured outputs aligned with common academic review practice: problem, method, results, limitations, and future directions.

## 3. Introduction
The rapid growth of academic and scientific publications has made it increasingly challenging for students, researchers, and professionals to keep up with available knowledge. Each year, large numbers of papers are published across multiple disciplines, making it difficult to read and analyze every document in detail. This leads to delayed literature screening, reduced productivity, and information overload in research and learning environments. The problem has been repeatedly emphasized in summarization surveys, which note that practical use still requires better document-level understanding and more reliable summaries for downstream decision-making [1], [2].

This challenge is important because academic performance and research quality depend on timely access to key contributions, methods, and findings. Manual full-paper reading remains valuable, but it is not always feasible when users need to process many papers in limited time. A reliable automated summarization assistant can support literature review, topic exploration, and faster comparison of studies.

Artificial Intelligence, particularly Natural Language Processing (NLP), provides suitable methods to address this challenge. Earlier neural methods established strong foundations for abstractive summarization [3], while pointer-generator mechanisms improved content selection and reduced some generation errors [4]. Transformer-based models then significantly improved contextual modeling and language quality through pretraining and transfer learning [5]-[8]. More recently, large language models and agent frameworks introduced task decomposition, controllable prompting, and structured generation workflows, which are useful for real-world task-oriented assistants [9]-[11].

The motivation of this project is to create a practical research paper summarization agent that is accurate, structured, and feasible for student deployment. The system is designed to process long papers through chunking and synthesis, then return a section-aware summary that helps users quickly understand core content without losing academic context.

## 4. Literature Review
Automatic text summarization has evolved from extractive ranking approaches to neural abstractive generation and, more recently, LLM-driven reasoning pipelines. Early abstractive neural models demonstrated that sequence-to-sequence learning can produce readable summaries, but they also showed weaknesses in factual consistency and long-context handling [3]. Pointer-generator networks improved grounding by allowing direct copying from source text, reducing some omissions and unsupported phrases [4]. These works established the transition from sentence extraction to generation-oriented summarization.

Transformer pretraining brought major quality gains. BERT improved contextual language understanding [5], T5 unified many NLP tasks under a text-to-text paradigm [8], PEGASUS introduced pretraining objectives specifically beneficial for summarization [6], and BART improved generation through denoising pretraining [7]. At a broader level, surveys report that these pretrained transformer families generally outperform earlier baselines in coherence, fluency, and coverage [2].

For long and scientific documents, however, difficulty remains. Research papers contain technical terms, section-level discourse, and long dependencies across abstract, methods, experiments, and conclusion. A discourse-aware model for long-document summarization showed that document structure must be modeled explicitly to improve quality, making it highly relevant as a baseline direction for academic paper summarization [12]. Recent review literature also confirms that long-document summarization remains a practical bottleneck even in modern systems [2].

Evaluation is another key issue. ROUGE remains widely used and useful for lexical overlap comparison [13], but it does not fully capture factual correctness, semantic adequacy, or readability in specialized domains. Recent LLM and agent surveys further emphasize that prompt engineering and multi-step orchestration can improve usefulness in real tasks, but reliability and hallucination control still require careful design [9]-[11].

To synthesize the literature for this proposal, Table 1 compares representative studies that shape the design of the proposed agent.

**Table 1. Comparative review of representative studies in summarization and LLM-based agent systems**
| Year | Study | Method | Key contribution | Limitation | Relevance to proposed work |
|---|---|---|---|---|---|
| 2004 | Lin [13] | ROUGE evaluation metric | Standardized automatic summary evaluation | Weak semantic and factual assessment | Motivates adding structure-focused and qualitative checks |
| 2016 | Nallapati et al. [3] | Seq2Seq RNN abstractive summarization | Strong neural baseline for abstractive generation | Limited long-document handling and factual reliability | Foundation for generation-based summarization |
| 2017 | See et al. [4] | Pointer-generator network | Better source grounding via copy mechanism | Still challenged by complex long technical text | Inspires content-preserving summarization behavior |
| 2017 | Allahyari et al. [1] | Summarization survey | Consolidates extractive and abstractive trends | Predates latest LLM generation advances | Establishes classical methods and gap evolution |
| 2018 | Devlin et al. [5] | BERT pretraining | Context-rich language representations | Not designed as end-to-end long-doc summarizer | Supports section-aware representation importance |
| 2018 | Cohan et al. [12] | Discourse-aware long-document summarization | Models scientific document structure for long inputs | Earlier architecture, limited modern LLM controllability | Serves as strong long-document scientific baseline reference |
| 2019 | Zhang et al. [6] | PEGASUS pretraining | Summarization-focused pretraining objective | Requires substantial compute/data | Justifies pretrained summarization prompts |
| 2019 | Lewis et al. [7] | BART denoising seq2seq | High-quality abstractive text generation | Hallucination risk in specialized domains | Supports abstractive synthesis stage |
| 2020 | Raffel et al. [8] | T5 text-to-text transformer | Unified transfer learning for generation tasks | Expensive for low-resource deployment | Motivates lightweight pipeline with free-tier API |
| 2023 | Zhang et al. [2] | Modern summarization survey | Comprehensive view of recent architectures | Persistent long-context and factuality issues | Directly supports identified research gaps |
| 2023 | Zhao et al. [9] | LLM survey | Broad analysis of LLM capabilities and limits | Not specific to scientific summarization pipelines | Supports LLM selection and risk discussion |
| 2023 | Xi et al. [10] | LLM agent survey | Agentic decomposition and tool-use perspectives | Limited direct benchmarking in academic summarization | Supports task-oriented agent architecture |
| 2024 | OpenAI GPT-4 report [11] | Frontier LLM technical report | Demonstrates strong generative reasoning capability | Cost and reliability constraints in deployment contexts | Motivates practical model-choice and safety constraints |

Across these studies, four consistent gaps are visible. First, long-document scientific summarization remains difficult despite strong language models [2], [12]. Second, fluent summaries may still omit critical technical details or introduce unsupported claims [3], [7], [9]. Third, lexical metrics alone cannot guarantee semantic and factual quality [13]. Fourth, high-performance models may be expensive or impractical for student-level deployment [8], [11].

The proposed system addresses these gaps through a task-oriented and structured pipeline. It combines chunk-based processing for long papers, prompt-based map-reduce synthesis for coherence, and section-wise output formatting tailored to academic use. This design directly aligns with evidence from prior work while remaining feasible for classroom implementation.

## 5. Material and Methods (Initial Phase)
### 5.1 Architecture Overview
The proposed pipeline is:  
User Query or Paper Upload -> Document Parser -> Text Cleaning -> Chunking Module -> Task-Aware Prompt Construction -> Gemini LLM (Map Stage) -> Chunk-Level Summaries -> Gemini LLM (Reduce Stage) -> Output Validation -> Structured Summary Output.

### 5.2 Methodology Details
In the first stage, the user provides a paper in PDF or TXT format. The parser extracts text and removes artifacts caused by layout or encoding noise. The cleaned document is then segmented into overlapping chunks to preserve context continuity while remaining within model token limits.

In the second stage, each chunk is processed through a map prompt that requests focused extraction of core scientific information. The intermediate outputs are then fused through a reduce prompt that generates a coherent final summary. This summary is formatted into fixed academic headings, including overview, problem statement, method, experimental setup, findings, limitations, and future work.

In the third stage, output validation checks for missing sections, unsupported claims, or overly vague statements. The system then returns the final structured response in markdown format so it can be directly used in literature review workflows or report drafting.

### 5.3 Rationale for Method Selection
The selected method is suitable because it handles long papers more reliably than single-pass summarization, reduces information loss through chunk overlap and synthesis, and produces outputs aligned with real academic reading behavior. The architecture is also practical for student implementation because it can run with a free-tier API while still demonstrating modern AI-agent design principles.

## 6. References
[1] M. Allahyari, S. Pouriyeh, M. Assefi, et al., "Text summarization techniques: A brief survey," International Journal of Advanced Computer Science and Applications, vol. 8, no. 10, pp. 397-405, 2017.

[2] Y. Zhang, P. Tiwari, X. Chen, et al., "Recent advances in text summarization: A survey," ACM Computing Surveys, vol. 55, no. 1, pp. 1-36, 2023.

[3] R. Nallapati, B. Zhou, C. Gulcehre, and B. Xiang, "Abstractive text summarization using sequence-to-sequence RNNs and beyond," arXiv:1602.06023, 2016.

[4] A. See, P. Liu, and C. D. Manning, "Get to the point: Summarization with pointer-generator networks," arXiv:1704.04368, 2017.

[5] J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova, "BERT: Pre-training of deep bidirectional transformers for language understanding," arXiv:1810.04805, 2018.

[6] J. Zhang, Y. Zhao, M. Saleh, and P. Liu, "PEGASUS: Pre-training with extracted gap-sentences for abstractive summarization," arXiv:1912.08777, 2019.

[7] M. Lewis, Y. Liu, N. Goyal, et al., "BART: Denoising sequence-to-sequence pre-training for natural language generation, translation, and comprehension," arXiv:1910.13461, 2019.

[8] C. Raffel, N. Shazeer, A. Roberts, et al., "Exploring the limits of transfer learning with a unified text-to-text transformer," Journal of Machine Learning Research, vol. 21, pp. 1-67, 2020.

[9] W. X. Zhao, K. Zhou, J. Li, et al., "A survey of large language models," arXiv:2303.18223, 2023.

[10] Z. Xi, W. Chen, X. Guo, et al., "The rise and potential of large language model based agents: A survey," arXiv:2309.07864, 2023.

[11] OpenAI, "GPT-4 Technical Report," arXiv:2303.08774, 2024.

[12] A. Cohan, F. Dernoncourt, D. S. Kim, T. Bui, S. Kim, W. Chang, and N. Goharian, "A discourse-aware attention model for abstractive summarization of long documents," in Proc. NAACL-HLT, 2018, pp. 615-621.

[13] C.-Y. Lin, "ROUGE: A package for automatic evaluation of summaries," in Proc. ACL Workshop, 2004, pp. 74-81.
