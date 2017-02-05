# ADAProject

Project Structure:

Swiss products - Our main notebook, were we work in pandas, and perform all the stats

Project - Swiss products on Amazon - Spark notebook with some exploratory analysis of the whole dataset

Companies list xtractor - Helper notebook to extract wikipedia lists

Product comparisons - Helper notebook with some experiments

Interactive viz - Helper notebook with some visualisations in bokeh 

Results - PDF with our interpretation of the results

companies - Folder with the extracted company lists

Spark_scripts - Folder with the final scripts we used on the cluster

Datasets - the extracted datasets we used

Charts - Folder with some static visualisations used in the posters 

Posters - Folder with the posters

_______________________________________________________________________________________
Abstract:   
The goal of our project is to study the perception of Swiss products around the world. To achieve this goal we will use a dataset of Amazon reviews all of which assign a rating of the product. Furthermore, we will take in consideration only relevant ratings based on the fact of whether people find them helpful or not.
Finally, we will use statistical tests to show if there is a significant difference between Swiss products and products from other countries in the same category.

Data description:     
The data set consists of around 550 thousand products from amazon. For each product, the data set contains the following information: Product id, Amazon Standard Identification Number, Title, Product group, Amazon sales rank, ASINs of co-purchased products, Location in product category hierarchy and Reviews. For the Reviews specifically, we have the average number of stars, the individual number of stars for all reviews and the number of people that found a review helpful.

Feasibility and Risks:     
The project should be feasibly completed within the required time frame as the data set is relatively small and all the manipulations we will perform are not computationally expensive. However, there is a very great risk that the data set does not contain sufficient data samples of Swiss products. In this case, we would possibly need to recrawl Amazon to extract more data samples or try to scrape the data from an existing crawl like the common crawl. In either case, this will probably take a substantial amount of time.

Deliverables:   
All the code used for the processing of the data.
Written report of the findings
Web site with a visualisation

Time plan:   
1.Processing the data set, additional crawling and dada preparation (Mid November - Mid December)   
2.Performing data analysis and statistical test on clean data (Mid December - End of December)   
3.Project website and summary (Beginning of January)   
 
