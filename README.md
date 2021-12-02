# project\_recommendations\_ibm

### Files
Recommendations\_with\_IBM\_submit.ipynb is the final version. Mostly debugged and refactored. (more to go)

Recommendations\_with\_IBM\.ipynb contains some original print info, debug info.

### TODO
- Documentation / Explanation.
- Deployment to an app.

### Approaches

- Exploratory Data Analysis
- Rank Based Recommendations
- User-User Based Collaborative Filtering
- Content Based Recommendations (EXTRA - NOT REQUIRED)
- Matrix Factorization
- Extras & Concluding

### Known Issues
There are some function order sequence related issues that might require re-order positions of functions
in order to run sequentially in a notebook. 

Otherwise, I need to manually jump up and down in the notebook file to 
execute functions that required by some callers. 

Further refactoring required. 

### Suggested Updates / Fixes

- For empty values (missing values), NaN, use fillna() could be much easier, rather than manually finding empty. For example, 
for Clean empty / missing page body and desc content. To update with fillna().
- For TFIDF (term frequency–inverse document frequency) similarity calculation, use dot product for calculation is also approachable.
Refer to book: "Hands-on Recommendation Systems with Python", section: "Computing the cosine similarity score", it mentions: 
"Fortunately, ... represented as TF-IDF vectors, their magnitude is always 1. Hence, we do not need to calculate the denominator in the cosine similarity formulal as it will always be 1. 
... reduced to computing the much simpler and computationally cheaper dot product. scikit-learn pairwise linear_kernel

