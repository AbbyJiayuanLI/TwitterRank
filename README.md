# Topic-sensitive TwitterRank
## Basic Idea
- We proposed a topic-sensitive ranking algorithm based on the existing TwitterRank Algorithm. 
- Based on the **topology level information** from TwitterRank, we further utilize the **top-specific information**, such as the comment preference or the number of tweets on specific topic, namely **expertness**, to obtain a more precise identification of individual influence.
- A **weighted Borda count** method is used to combine this two rankings.

## Testing
- Testing is performed on real twitter data to compute individual influence, and is combined with individual comments to predict real-time box office prediction.
