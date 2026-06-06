# Final Research Report: Magi Model for Manga Diarisation

## 1. Paper Overview
This paper introduces "Magi," a unified, two-stage AI architecture designed to automate manga analysis and transcription. The primary motivation for the research is to bridge the accessibility gap for individuals with visual impairments (PVI), who require scene descriptions, transcriptions, and character identity mapping to consume manga effectively. The model transforms complex manga pages into structured, readable, or audible transcripts, effectively performing "manga diarisation"—the identification of speakers and the sequencing of dialogue in the correct reading order.

## 2. Problem Statement
Manga is a globally popular medium that remains largely inaccessible to PVI. Previous research indicates that PVI prioritize scene descriptions, dialogue transcriptions, and character facial expressions. However, automating these tasks is highly complex due to the inherent challenges of the manga medium, including:
*   Varying artistic styles and image resolutions.
*   Non-human characters and complex occlusions.
*   Inconsistent associations between speech balloons and speakers.
*   Unconventional page layouts and non-linear reading paths.

## 3. Proposed Method
Magi employs a two-stage unified architecture that treats manga page components as a graph generation problem, followed by a transcription process based on layout knowledge:

*   **Graph-Based Detection:** The model detects panels, text blocks, and character boxes, establishing these as nodes within a graph.
*   **Speaker Association:** Relationships between detected text blocks and characters are defined as edges in the graph. The system uses bipartite graph matching to associate dialogue with specific speakers.
*   **Character Clustering:** The model clusters character boxes by identity without requiring prior knowledge of the total number of characters (identity count) in a scene.
*   **Reading Order Sorting:** A novel approach is implemented to organize text blocks into the correct sequence, ensuring the transcript reflects the narrative flow.
*   **Architecture Efficiency:** The two-stage design provides a more lightweight alternative to traditional end-to-end models.

## 4. Data and Experimental Setup
*   **Benchmark Dataset:** The authors developed "PopManga," an annotated evaluation benchmark consisting of pages from over 80 popular manga titles.
*   **Standard Reference:** The research references the "Manga109" dataset (containing over 21,000 images) as a foundational resource for panel, text, and character detection research.
*   **Training Techniques:** Methodologies discussed in the literature review include transfer learning for character detection, unsupervised clustering for re-identification, and SimCLR-style training to handle both face and body character crops.

## 5. Main Results
*   **Diarisation Capability:** Magi successfully automates the identification of speakers, the clustering of character identities, and the association of dialogue with the correct speakers.
*   **Transcription:** The model generates coherent dialogue transcripts that follow the correct narrative reading order.
*   **Performance:** Magi demonstrates superior performance compared to existing approaches on the PopManga benchmark.
*   **Visualization:** The model can visually map character identity associations by drawing line connections between the centers of character boxes and their associated text.

## 6. Strengths
*   **Unified Approach:** By moving from detection to graph-based association, the model simplifies a highly complex set of tasks into a cohesive, two-stage process.
*   **Accessibility Focus:** The model directly addresses a significant social need by converting visual manga content into accessible text formats.
*   **Flexibility:** The character clustering method functions without needing pre-defined cluster counts, making it adaptable to varying scenes.

## 7. Limitations
*   Manga understanding remains inherently difficult due to artistic variance, complex layouts, and inconsistent visual cues.
*   Specific quantitative limitations regarding model accuracy, inference speed, or edge-case failure rates are not clearly stated in the provided text.

## 8. Future Work
*   Not clearly stated in the provided text.

## 9. 5-Bullet Ultra-Short Summary
*   **Magi** is a new AI model that automates manga diarisation for visually impaired readers.
*   The system uses a **two-stage graph-based architecture** to detect, cluster, and associate characters with dialogue.
*   It successfully generates coherent, ordered transcripts from complex manga page layouts.
*   A new benchmark, **PopManga**, was created to evaluate the model using over 80 popular manga titles.
*   The research addresses critical accessibility gaps by translating visual storytelling into structured, text-based data.