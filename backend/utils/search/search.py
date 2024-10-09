from utils.helper import index_pinecone_embedding

def get_surrounding_frames(frame_id, frame_name, video_name, window=50):
    # Initialize Pinecone index
    index = index_pinecone_embedding()
    
    # Define filter to get the next 50 frames (frames with frame_name > current frame_name)
    metadata_filter_01 = {
        "video_name": video_name,
        'frame_name': {"$gt": frame_name}
    }
    # Query for next 50 frames
    query_results_01 = index.query(
        id=frame_id,
        filter=metadata_filter_01,
        top_k=window,
        include_metadata=True,
        include_values=False
    )
    
    # Define filter to get the previous 50 frames (frames with frame_name <= current frame_name)
    metadata_filter_02 = {
        "video_name": video_name,
        'frame_name': {"$lte": frame_name}
    }
    # Query for previous 50 frames
    query_results_02 = index.query(
        id=frame_id,
        filter=metadata_filter_02,
        top_k=window,
        include_metadata=True,
        include_values=False
    )
    
    # Combine results from both queries
    # final_result = {
    #     "previous_frames": query_results_02['matches'],
    #     "next_frames": query_results_01['matches']
    # }

    rsl = dict()
    match_list = []
    matches_1 = query_results_01['matches']
    for match in range(len(matches_1)):
        match_list.append(matches_1[match])

    matches_2 = query_results_02['matches']
    for i in range(len(matches_2)):
        match_list.append(matches_2[i])
    

    final_result = {"matches": match_list}
    print("FINAL RESULT: ", final_result)
    return final_result