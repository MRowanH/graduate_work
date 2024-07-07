# CSCE 5222: Feature Engineering Project Proposal
# Due: October 18th, 2022


## Project Title and Team Members
* Team Members: Andrew Fausak, Andy Fausak, Andre Sharp, Mica Haney
* Project Title: Audio Analysis Using Gramian Angular Field (GAF) and FAST

## Idea description
* Summarizing Text and Speach is complex.  Moreover, performing search methods to find similarity between works is difficult.  Having a convenient way to produce feature extraction from a given set of text or audio files to represent overal structure and content of the work is desired. Using NLP tools to feed GAF generator for creating a special feature tag reprsenting the overall structure and content of a work is the goal of this effort.  This will in itself provide NLP Analysis of audio file and convert to GAF with FAST compatiblity to ultimately generate a visual object representing the content of text or audio file.

## Goals and Objectives:
* Can GAF be used in a QR-code-like rendering for the identification characterization of audio files (mp3/wav), and creating a unique “fingerprint”?
* Plan is to convert audio
* (as full intelligence)-> GAF image -> Feature Extraction -> audio (as reference feature)
    ```mermaid
    flowchart LR
        id1[original audio from dataset as full intelligence]-->id2[Feature Extraction]
        id2[Feature Extraction]-->id3[GAF Image]
        id3[GAF Image]-->id2[Feature Extraction]
        id2[Feature Extraction]-->id4[Extracted Audio]
    ```
* Identify usability with FAST keypoints for audio files, and ability to detect plagiarism between audio files.
* Identify possibility of converting a GAF back to an Audio File 

## Motivation
* Motivation to create this work is based on review of a pollution analysis method that utilizes GAF to provide images representing normalized discrete readings in summary, thereby enabling tools to perform similarity tests to qualify conditions needing to be monitored.  Having a solution whereby similarity of works can be compared is useful and readily consumed by AI tools needing features to isolate desired inferences. Experimentation is required to determine resolution needed to uniquely identify or classify a work using NLP methods. Converting data from one domain of information representation to another can provide useful information that would not otherwise be noticable, such as in spectrograms. People have hidden "text" and images in sound files that can be identified only by using specific graphical tools. Using graphical processing techniques to find hidden information in audio is an interesting topic with the potential to improve the current methods of working with audio.

## Significance
* Having a means to identify works quickly in terms of classification and/or origin is very useful.  Moreover, this may provide alternate means of tagging documents for referencing. With this technique more information may be extracted from the audio, which will allow for better handling of audio tasks. If the proposed method does extract information from sound that is not usually or easily picked up by current audio processing techniques, then adding such features and procedures could notably improve results involving audio, particularly in machine learning models. Additionally, if the proposed technique works then this is a potentially novel way of performing speech recognition (pending further research).

## Literature Survey
* Different domains were identified using GAF.  However, applications specific to NLP have not been identified.  There was not any other research on this topic we were able to find.  There is a lot of research on using a time series with GAF, however, nothing has been noted in regard to audio files.

## Features
* Initial Audio Files Dataset
* Initial Generated Text

## GAF Images
* FAST keypoints are identification with GAF
* Plagiarism Detection with GAF
* Final Generated Audio File
* Final Generated Text
* Classification
* Tagging

## Expected Outcome 
* Identify the usefulness of a GAF for Natural Langauge methods such as Audio and Text Files.  What is the loss?  How well does this method classify or provide unique tagging for a work?  Does this make a difference in classification methods? At the end of the project we expect to be able to answer these questions. We also expect to find that we will be able to extract and/or generate text from audio files where this is relevent to the file.

## References 
* https://www.mdpi.com/1263342
* https://www.kaggle.com/datasets/alanchn31/free-spoken-digits

## Github Link:
* https://github.com/dallasai/csce5222-project
