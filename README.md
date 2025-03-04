# Video Retrieval System with Image Embeddings and RAG
## Overview
This project introduces an advanced video retrieval system that efficiently processes and indexes video content for rapid and precise search queries. The system integrates keyframe extraction, object detection, and multimodal embeddings to enhance video retrieval capabilities. Users can retrieve relevant video moments using textual descriptions, images, or metadata-based queries. 
## Features
- **Multimodal Video Retrieval** – Supports searching for video frames using **text, images, and transcripts**.  
- **Keyframe Extraction** – Uses **PySceneDetect** for scene detection and **MobileNetV3** for duplicate removal.  
- **Image Embeddings** – Utilizes **BEiT-3** to convert video frames into searchable vector representations.  
- **Object Detection & Metadata** – Detects objects with **Mask R-CNN**, extracts **color, position, and labels**, and associates metadata with each frame.  
- **OCR Processing** – Recognizes text within frames using **VinOCR-1B** for Vietnamese OCR.  
- **Transcript-Based Search** – Processes video audio using **Whisper-3** for speech-to-text conversion and stores transcript embeddings using **Alibaba-NLP**.  
- **Retrieval-Augmented Generation (RAG)** – Enhances search results by **re-ranking and filtering** key video segments.  
- **Flexible Query System** – Users can search via:  
   - **Text queries** (keywords, descriptions)  
   - **Image-based search** (finding similar frames)  
   - **Transcript-based retrieval** (searching spoken content)  
   - **Object-based filtering** (finding frames with specific objects, colors, and attributes)  
- **User-Friendly Interface** – Provides a **web-based GUI** with interactive filtering, query input, and export options.  
- **Efficient Vector Database** – Stores processed data in **cloud storage** for **fast, large-scale retrieval**.  

## Install guide
- To set up the environment, follow the installation steps for both frontend and backend 
- Ensuring GPU availability for optimal performance.
 1. Clone the Repository
    ``` bash
    
    ```
    
The backend is implemented in Python with deep learning models for content processing, while the frontend offers an intuitive interface for seamless user interactions. 
