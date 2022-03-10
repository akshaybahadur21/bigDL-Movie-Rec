<div align="center">

<p align="center"> <img src="https://bigdl-project.github.io/img/bigdl_logo.png" height="140px"><br></p>

**Building Large-Scale AI Applications for Distributed Big Data**

</div>

---

# BigDL Movie Recommendation System

BigDL is a distributed deep learning library for Apache Spark; with BigDL, users can write their deep learning applications as standard Spark programs, which can directly run on top of existing Spark or Hadoop clusters.

- **Rich deep learning support:** Modeled after Torch, BigDL provides comprehensive support for deep learning, including numeric computing (via Tensor) and high level neural networks; in addition, users can load pre-trained Caffe or Torch models into Spark programs using BigDL.
- **Extremely high performance:** To achieve high performance, BigDL uses Intel oneMKL, oneDNN and multi-threaded programming in each Spark task. Consequently, it is orders of magnitude faster than out-of-box open source Caffe or Torch on a single-node Xeon (i.e., comparable with mainstream GPU).
- **Efficiently scale-out:** BigDL can efficiently scale out to perform data analytics at "Big Data scale", by leveraging Apache Spark (a lightning fast distributed data processing framework), as well as efficient implementations of synchronous SGD and all-reduce communications on Spark.


### Notebooks
- [Colab BigDL](https://colab.research.google.com/drive/1c-Qh6GHigYbb_8zxjDGbjbx7ivN1UKs4?usp=sharing)
