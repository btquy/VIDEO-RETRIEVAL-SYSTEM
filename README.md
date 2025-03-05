# Video Retrieval System with Image Embeddings and RAG

## Overview
This project introduces an advanced video retrieval system that efficiently processes and indexes video content for fast and accurate search queries for the [AI ​​Challenge HCM 2024](https://aichallenge.hochiminhcity.gov.vn). The system integrates keyframe extraction, object detection, and multimodal embedding to enhance video retrieval. Users can retrieve relevant video moments using text descriptions, images, or metadata-based queries. 

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
 ### 1. Clone the Repository
``` 
git clone https://github.com/btquy/VIDEO-RETRIEVAL-SYSTEM.git
```
### 2. Install Required Libraries
- Negative frontend the folder and run the following cammand
```
pnpm install
pnpm dev
```
The frontend offers an intuitive interface for seamless user interactions. 
- With Backend folder
```
pip install -r requirement.txt
python main.py
```
The backend is implemented in Python with deep learning models for content processing. 

## User Interface
- When build success, you can see the following interface 

![User Interface](https://github.com/btquy/VIDEO-RETRIEVAL-SYSTEM/raw/efb88385482ef207af10cdf8ef8556e020180fcc/User_interface_2.png)

- **(1)** Users can enter text inquiries or review transcripts in the left query field.
- **(2)** This tool lets users filter results by label name, color, frame location, and several labels and store the selected item information.  
- **(3)** The central panel displays a grid of photos showing all inquiry input frames. Each frame offers two options: ‘move to top‘ and ‘delete.‘  
- **(4)** "Search," "Submit," and "Export" buttons at the bottom let users finish their actions.

![User Interface](https://github.com/btquy/VIDEO-RETRIEVAL-SYSTEM/raw/efb88385482ef207af10cdf8ef8556e020180fcc/User_interface_2.png)

- Secondary interfaces may enlarge any main screen frame. This layout has six primary parts:
  
(1) shows the frame and video to help customers understand their request.   
(2)(6) enable complicated searches for comparable frames and better replies.   
Frame or video from (1) appears on screen (3).  
(4) shows information on the right, while Part  
(5) accepts replies. Q&A mode generates contest organizer-compliant answers. 
