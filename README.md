<div align="center">

<p align="center"> <img src="https://bigdl-project.github.io/img/bigdl_logo.png" height="140px"><br></p>

**Building Large-Scale AI Applications for Distributed Big Data**

</div>

---

# BigDL Movie Recommendation System 🎬

BigDL is a distributed deep learning library for Apache Spark; with BigDL, users can write their deep learning applications as standard Spark programs, which can directly run on top of existing Spark or Hadoop clusters.

- **Rich deep learning support:** Modeled after Torch, BigDL provides comprehensive support for deep learning, including numeric computing (via Tensor) and high level neural networks; in addition, users can load pre-trained Caffe or Torch models into Spark programs using BigDL.
- **Extremely high performance:** To achieve high performance, BigDL uses Intel oneMKL, oneDNN and multi-threaded programming in each Spark task. Consequently, it is orders of magnitude faster than out-of-box open source Caffe or Torch on a single-node Xeon (i.e., comparable with mainstream GPU).
- **Efficiently scale-out:** BigDL can efficiently scale out to perform data analytics at "Big Data scale", by leveraging Apache Spark (a lightning fast distributed data processing framework), as well as efficient implementations of synchronous SGD and all-reduce communications on Spark.

## Description 🍿
Recommendation System is a filtration program whose prime goal is to predict the “rating” or “preference” of a user towards a domain-specific item or item. 
 In our case, this domain-specific item is a movie, therefore the main focus of our recommendation system is to filter and predict only those movies which a user would prefer given some data about the user him or herself


## Notebooks
- [Colab BigDL](https://colab.research.google.com/drive/1c-Qh6GHigYbb_8zxjDGbjbx7ivN1UKs4?usp=sharing)

## Execution 🐉

```streamlit run streamlit-movie-rec.py```

**[Streamlit Hosted Movie Recommendation](https://share.streamlit.io/akshaybahadur21/bigdl-movie-rec/main/streamlit-movie-rec.py)**

## Results 📊

## Team 🏆

- Akshay Bahadur
- Ayush Agarawal

#### Made with ❤️ and 🦙 by Akshay and Ayush


## References 🔱
- [Recommendation System Recitation from Spring 2020](https://github.com/ckaestne/seai/blob/S2020/recitations/06_Collaborative_Filtering.ipynb)
- [Introduction to Recommender System - Shuyu Luo](https://towardsdatascience.com/intro-to-recommender-system-collaborative-filtering-64a238194a26)
- [Streamlit](https://streamlit.io/)
