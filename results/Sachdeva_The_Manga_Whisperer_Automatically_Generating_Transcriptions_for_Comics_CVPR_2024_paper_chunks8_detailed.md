# Final Research Report: Magi Model for Manga Diarisation

## 1. Paper Overview
This paper introduces **Magi**, a unified AI model developed to automate the diarisation of manga. Manga diarisation involves determining "who said what and when," which is critical for making manga accessible to People with Visual Impairments (PVI). By leveraging computer vision and deep learning, the model processes entire manga pages to generate coherent transcripts, effectively closing the accessibility gap in a medium previously lacking dedicated assistive technology.

## 2. Problem Statement
Despite the global popularity of manga, it remains largely inaccessible to PVI. Previous research indicates that PVI readers specifically require scene descriptions, character identities, and accurate transcriptions to engage with the medium. Automating these tasks is highly complex due to:
*   Varying artistic styles and occlusions.
*   The presence of non-human characters.
*   Ambiguous speech balloon tails and variable text placement.
*   The necessity for high-level deductive reasoning to determine reading order and speaker-text association.

## 3. Proposed Method
Magi employs a two-stage unified architecture that treats manga analysis as a graph generation problem.

*   **Architecture:** The model utilizes a CNN-based backbone for spatial feature extraction, followed by a DETR-style transformer (encoder-decoder) to process dense feature descriptors across the entire page rather than individual crops.
*   **Detection:** Specialized detection heads identify panels, text blocks, and character boxes.
*   **Graph Generation:** Detections are treated as nodes in a graph. The model uses dedicated tokens to predict edges:
    *   **[C2C] tokens:** Used for character-character clustering based on identity, enabling unsupervised clustering without predefined identity counts.
    *   **[T2C] tokens:** Used to associate specific dialogue (text blocks) with their respective speakers.
*   **Transcription:** Following graph generation, the model utilizes prior knowledge of manga layout structures to sort text boxes into the correct reading order to produce a final transcript.

## 4. Data and Experimental Setup
*   **Benchmark:** The authors introduced the **PopManga** benchmark, which consists of annotated pages from 80+ popular and complex manga titles to evaluate the model's performance.
*   **Context:** The system leverages the **Manga109** dataset (containing over 21,000 images) as a foundational resource for training panel, text, and character detection.
*   **Techniques:** The framework incorporates domain adaptation, transfer learning, and SimCLR-style modeling to handle the variety in character representation.

## 5. Main Results
*   **Automated Diarisation:** Magi successfully automates the full diarisation pipeline, outputting coherent transcripts that can be read or listened to by users.
*   **Superior Performance:** The model demonstrates superior performance compared to existing prior works.
*   **Clustering:** The system effectively clusters characters by identity without requiring prior knowledge of the number of characters present.
*   **Visualization:** Magi can visualize detected components, including the linkage between specific character identities and their corresponding speech balloons.

## 6. Strengths
*   **Unified Pipeline:** By moving away from end-to-end architectures toward a two-stage graph-based approach, the model maintains a lighter footprint while improving task accuracy.
*   **In-context Processing:** Processing the entire page simultaneously (rather than through individual character crops) allows for better use of global spatial context, which is essential for accurate speaker association.
*   **Accessibility Focus:** Directly addresses a specific societal need for PVI accessibility through concrete, usable technical outputs (transcripts).

## 7. Limitations
*   **Complexity of Association:** While detection tasks are considered straightforward, character-to-character association remains a "tricky" and challenging technical hurdle.
*   **Contextual Constraints:** Previous metric-learning-based approaches for character re-identification were limited by their focus on isolated crops; while Magi addresses this with global context, the task remains inherently difficult due to artistic variance.
*   **General Limitations:** Not clearly stated in the provided text.

## 8. Future Work
Not clearly stated in the provided text.

## 9. 5-Bullet Ultra-Short Summary
*   **Magi** is a unified AI model designed to automate manga diarisation for visually impaired readers.
*   The model treats manga analysis as a **graph generation problem**, linking detected panels, text, and characters.
*   It utilizes a **DETR-based transformer** to process entire manga pages for superior spatial context.
*   The system includes a new benchmark, **PopManga**, comprising over 80 complex manga volumes.
*   Magi effectively performs unsupervised character clustering and associates dialogue with speakers to produce coherent transcripts.