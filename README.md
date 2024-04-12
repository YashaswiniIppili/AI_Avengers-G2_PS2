# AI_Avengers-G2_PS2
Team Name : AI Avengers <br>
Problem Statement 2
<br>
Video Link : https://drive.google.com/file/d/1BhweMMM39sdqVBBkoyz3xXFYUDQ-xU8f/view?usp=sharing

# Problem Statement
G2 has more than 2.5 million reviews for various products and services. These reviews help both buyers and software vendors in decision-making. One interesting aspect of the review data that we want to solve is to list the exact feature sets the customers are looking for. A few examples include application performance, the overall user experience, missing functionality, bugs, etc. As an aspiring Computer Science graduate, we would like you to develop a system that analyses the review data for a particular product from G2 using the API provided below and provides a list of feature sets that the customers are looking for. Here's the API endpoint that you can use:

https://data.g2.com/api/docs#reviews-list - You can use this batch API to fetch reviews of G2 Marketing solutions in a batch of 100 using the page[size] param. Once you have accumulated all reviews, use an algorithm to find the customer asks. The results can be printed on the console.

# Proposed Solution
1. **Data Extraction:** Data is extracted in JSON format from the API endpoint using the provided API key.<br>
2. **Conversion to CSV:** The JSON file is converted into a CSV file for easier processing and analysis.<br>
3. **Sentiment Analysis:** Sentiment analysis is applied to the data to identify top positive and negative comments. This helps in understanding customer preferences and areas for improvement.<br>
4. **Machine Learning Model Training:** The sentiment analysis results and original data are sent to a Language Model (LLM) for training. This step enhances the accuracy of predictions by leveraging machine learning.
5. **Interactive Web Application:** Gradio is utilized to create an interactive web chat application interface. This interface enables users to perform various analyses on the provided data swiftly and accurately

Overall This Proposed does 2 processes :
1) Sentiment analysis using NLP on the data and reviews provided
2) Sending the Sentiment analysis alone with the Review data to an LLM to be trained upon.

This will make the model way accurate than just training the model on the data or the reviews as now it knows the the top positve comments and top negative comments which it can use to decide the customer likes and customer asks with great accuracy.

<img width="849" alt="Screenshot 2024-04-13 at 12 07 26 AM" src="https://github.com/YashaswiniIppili/AI_Avengers-G2_PS2/assets/107344920/e2a4b81d-1974-4181-a775-aba518b693fa">


# How to Use 
1. To use the repo first clone the repo <br>
    ```

    git clone https://github.com/YashaswiniIppili/AI_Avengers-G2_PS2.git
  
    ```

2. Obtain API access and key, from G2 and replace the API-KEY with your api key in the fetch.py File
   ```
   
   secret_token = "API-KEY"
   
   ```
   After replacing run
   ```

   python3 fetch.py

   ```
3. Convert the json file you got into a csv file.
4. After you have the dataset Open a Jupiter Notebook and open both the ipynb files provided in 2 different notebooks
5. Run all the cells in the G2NLP.ipynb file, this file will do the sentiment analysis and the Preprocessing of the data for the LLM part of the project, **DO NOT FORGET TO CHANGE THE PATH OF THE DATASET TO THE EXTRACTED DATASET**
6. After running the G2NLP.ipynb you'll have a new dataset called merged.csv, and the sentimemt analysis done on the data also printing the top positive comments and top negatove comments
   
  ![image](https://github.com/YashaswiniIppili/AI_Avengers-G2_PS2/assets/107344920/31ac614a-6815-4158-8062-bf90b5c20b0f)

  ![image](https://github.com/YashaswiniIppili/AI_Avengers-G2_PS2/assets/107344920/f3991361-0e83-4708-bb1e-e858dc4297e7)


7. Now run all the cells of G2LLM.ipynb with the **dataset path as the path of merged.csv** on your local computer
8. Open the link the gradio provides to go the interactive AI powered chat bot.
9. We are using Meta-LLAMA-2-7b Model as our LLM model with sentence transformers to compute the embeddings (dense vector representations) for sentences.
10. Now let the model train on the data provided (this process speed will differ based on the computational power of the local computer)

    Now the mode provides results like this about the Reviews data, making customer review analysis Easier and Faster 
    
![image](https://github.com/YashaswiniIppili/AI_Avengers-G2_PS2/assets/107344920/75755d99-dabb-4c86-8868-6afeab79f6a8)

![image](https://github.com/YashaswiniIppili/AI_Avengers-G2_PS2/assets/107344920/acb9e0b3-b8f7-4f93-a751-605146da013c)

    

