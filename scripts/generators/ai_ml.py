"""
==============================================================
ARTIFICIAL INTELLIGENCE & MACHINE LEARNING GENERATOR
Version 3.0
==============================================================

Purpose:
    Curated AI and Machine Learning concepts for the
    Intelligent Educational Assistant.

Architecture:
    Uses common.py to generate structured educational
    knowledge families while preserving the existing
    knowledge-base schema.
"""

from __future__ import annotations

from .common import build_knowledge_family


CATEGORY = "Artificial Intelligence and Machine Learning"


# ============================================================
# CURATED AI / ML CONCEPTS
# ============================================================

CONCEPTS = [

    # ========================================================
    # AI FOUNDATIONS
    # ========================================================

    ("Artificial Intelligence", ["AI", "artificial intelligence"]),
    ("AI System", ["intelligent system"]),
    ("Intelligent Agent", ["AI agent"]),
    ("Rational Agent", ["rational intelligent agent"]),
    ("AI Problem Solving", ["artificial intelligence problem solving"]),
    ("Knowledge Representation", ["knowledge representation in AI"]),
    ("Automated Reasoning", ["AI reasoning"]),
    ("Machine Reasoning", ["computational reasoning"]),
    ("AI Planning", ["automated planning"]),
    ("Search in Artificial Intelligence", ["AI search"]),
    ("State Space Search", ["state space"]),
    ("Heuristic Search", ["heuristic algorithms"]),
    ("Artificial Intelligence Applications", ["AI applications"]),
    ("Artificial Intelligence Ethics", ["AI ethics"]),
    ("Responsible Artificial Intelligence", ["responsible AI"]),
    ("Explainable Artificial Intelligence", ["XAI", "explainable AI"]),
    ("Trustworthy Artificial Intelligence", ["trustworthy AI"]),

    # ========================================================
    # MACHINE LEARNING FOUNDATIONS
    # ========================================================

    ("Machine Learning", ["ML", "machine learning"]),
    ("Machine Learning Model", ["ML model"]),
    ("Machine Learning Algorithm", ["ML algorithm"]),
    ("Machine Learning Pipeline", ["ML pipeline"]),
    ("Machine Learning Dataset", ["ML dataset"]),
    ("Training Data", ["training dataset"]),
    ("Testing Data", ["test dataset"]),
    ("Validation Data", ["validation dataset"]),
    ("Training Set", ["training set"]),
    ("Testing Set", ["test set"]),
    ("Validation Set", ["validation set"]),
    ("Feature", ["machine learning feature"]),
    ("Feature Vector", ["feature representation"]),
    ("Target Variable", ["target"]),
    ("Label", ["data label"]),
    ("Instance", ["data instance"]),
    ("Sample", ["machine learning sample"]),
    ("Training", ["model training"]),
    ("Inference", ["model inference"]),
    ("Prediction", ["machine learning prediction"]),
    ("Model Evaluation", ["ML model evaluation"]),

    # ========================================================
    # TYPES OF MACHINE LEARNING
    # ========================================================

    ("Supervised Learning", ["supervised machine learning"]),
    ("Unsupervised Learning", ["unsupervised machine learning"]),
    ("Semi Supervised Learning", ["semi-supervised learning"]),
    ("Self Supervised Learning", ["self-supervised learning"]),
    ("Reinforcement Learning", ["RL"]),
    ("Online Learning", ["incremental learning"]),
    ("Batch Learning", ["batch machine learning"]),
    ("Transfer Learning", ["knowledge transfer"]),
    ("Active Learning", ["active machine learning"]),
    ("Federated Learning", ["federated machine learning"]),

    # ========================================================
    # CLASSIFICATION
    # ========================================================

    ("Classification", ["machine learning classification"]),
    ("Binary Classification", ["two-class classification"]),
    ("Multiclass Classification", ["multi-class classification"]),
    ("Multilabel Classification", ["multi-label classification"]),
    ("Logistic Regression", ["logistic regression classifier"]),
    ("Decision Tree Classifier", ["decision tree"]),
    ("Random Forest Classifier", ["random forest"]),
    ("Support Vector Machine", ["SVM"]),
    ("K Nearest Neighbors", ["KNN"]),
    ("Naive Bayes", ["Naive Bayes classifier"]),
    ("Gradient Boosting", ["gradient boosting classifier"]),
    ("AdaBoost", ["adaptive boosting"]),
    ("Bagging", ["bootstrap aggregation"]),
    ("Nearest Neighbor Classification", ["nearest neighbor"]),

    # ========================================================
    # REGRESSION
    # ========================================================

    ("Regression", ["machine learning regression"]),
    ("Linear Regression", ["linear regression model"]),
    ("Multiple Linear Regression", ["multiple regression"]),
    ("Polynomial Regression", ["polynomial regression"]),
    ("Ridge Regression", ["ridge"]),
    ("Lasso Regression", ["lasso"]),
    ("Elastic Net Regression", ["elastic net"]),
    ("Regression Analysis", ["predictive regression"]),
    ("Regression Prediction", ["continuous prediction"]),

    # ========================================================
    # CLUSTERING
    # ========================================================

    ("Clustering", ["machine learning clustering"]),
    ("K Means Clustering", ["K-means"]),
    ("Hierarchical Clustering", ["hierarchical cluster analysis"]),
    ("Agglomerative Clustering", ["agglomerative clustering"]),
    ("DBSCAN", ["density based clustering"]),
    ("Gaussian Mixture Model", ["GMM"]),
    ("Cluster Analysis", ["cluster analysis"]),

    # ========================================================
    # DIMENSIONALITY REDUCTION
    # ========================================================

    ("Dimensionality Reduction", ["dimension reduction"]),
    ("Principal Component Analysis", ["PCA"]),
    ("Linear Discriminant Analysis", ["LDA"]),
    ("Feature Extraction", ["feature extraction"]),
    ("Feature Selection", ["feature selection"]),
    ("Manifold Learning", ["manifold learning"]),
    ("Autoencoder", ["representation learning"]),

    # ========================================================
    # DECISION TREES AND ENSEMBLES
    # ========================================================

    ("Decision Tree", ["decision tree algorithm"]),
    ("Decision Tree Root", ["tree root"]),
    ("Decision Tree Node", ["tree node"]),
    ("Decision Tree Leaf", ["leaf node"]),
    ("Random Forest", ["random forest algorithm"]),
    ("Ensemble Learning", ["ensemble machine learning"]),
    ("Boosting", ["boosting algorithm"]),
    ("Bagging", ["bagging algorithm"]),
    ("Gradient Boosting Machine", ["GBM"]),
    ("XGBoost", ["extreme gradient boosting"]),
    ("LightGBM", ["light gradient boosting"]),
    ("CatBoost", ["categorical boosting"]),

    # ========================================================
    # MODEL PERFORMANCE
    # ========================================================

    ("Accuracy", ["classification accuracy"]),
    ("Precision", ["positive predictive value"]),
    ("Recall", ["sensitivity"]),
    ("Specificity", ["true negative rate"]),
    ("F1 Score", ["F1 measure"]),
    ("Confusion Matrix", ["classification confusion matrix"]),
    ("ROC Curve", ["receiver operating characteristic"]),
    ("AUC", ["area under curve"]),
    ("Precision Recall Curve", ["PR curve"]),
    ("Mean Absolute Error", ["MAE"]),
    ("Mean Squared Error", ["MSE"]),
    ("Root Mean Squared Error", ["RMSE"]),
    ("R Squared", ["coefficient of determination"]),
    ("Cross Validation", ["cross-validation"]),
    ("K Fold Cross Validation", ["k-fold"]),
    ("Stratified Cross Validation", ["stratified k-fold"]),

    # ========================================================
    # MODEL PROBLEMS
    # ========================================================

    ("Overfitting", ["model overfitting"]),
    ("Underfitting", ["model underfitting"]),
    ("Bias", ["machine learning bias"]),
    ("Variance", ["model variance"]),
    ("Bias Variance Tradeoff", ["bias-variance tradeoff"]),
    ("Data Leakage", ["machine learning data leakage"]),
    ("Model Drift", ["ML model drift"]),
    ("Concept Drift", ["concept drift"]),
    ("Distribution Shift", ["data distribution shift"]),
    ("Class Imbalance", ["imbalanced dataset"]),
    ("Noise", ["data noise"]),
    ("Outlier in Machine Learning", ["ML outlier"]),

    # ========================================================
    # FEATURE ENGINEERING
    # ========================================================

    ("Feature Engineering", ["ML feature engineering"]),
    ("Feature Scaling", ["feature normalization"]),
    ("Standardization", ["z-score scaling"]),
    ("Normalization", ["min-max normalization"]),
    ("One Hot Encoding", ["one-hot encoding"]),
    ("Label Encoding", ["label encoding"]),
    ("Ordinal Encoding", ["ordinal encoding"]),
    ("Feature Transformation", ["feature transformation"]),
    ("Feature Selection Method", ["feature selection methods"]),
    ("Feature Importance", ["feature importance"]),
    ("Missing Value Imputation", ["missing data imputation"]),

    # ========================================================
    # NEURAL NETWORKS
    # ========================================================

    ("Neural Network", ["artificial neural network"]),
    ("Artificial Neural Network", ["ANN"]),
    ("Neuron", ["artificial neuron"]),
    ("Perceptron", ["single-layer perceptron"]),
    ("Input Layer", ["neural network input layer"]),
    ("Hidden Layer", ["neural network hidden layer"]),
    ("Output Layer", ["neural network output layer"]),
    ("Weight in Neural Network", ["neural network weights"]),
    ("Bias in Neural Network", ["neural network bias"]),
    ("Activation Function", ["neural activation"]),
    ("Sigmoid Function", ["sigmoid"]),
    ("ReLU", ["rectified linear unit"]),
    ("Leaky ReLU", ["leaky rectified linear unit"]),
    ("Tanh Activation", ["hyperbolic tangent"]),
    ("Softmax Function", ["softmax"]),
    ("Forward Propagation", ["forward pass"]),
    ("Backpropagation", ["backward propagation"]),
    ("Gradient Descent", ["gradient optimization"]),
    ("Learning Rate", ["neural network learning rate"]),
    ("Loss Function", ["objective function"]),
    ("Epoch", ["training epoch"]),
    ("Batch Size", ["mini-batch"]),
    ("Optimizer", ["neural network optimizer"]),
    ("Adam Optimizer", ["Adam"]),
    ("Stochastic Gradient Descent", ["SGD"]),

    # ========================================================
    # DEEP LEARNING
    # ========================================================

    ("Deep Learning", ["deep neural networks"]),
    ("Deep Neural Network", ["DNN"]),
    ("Convolutional Neural Network", ["CNN"]),
    ("CNN Convolution", ["convolution operation"]),
    ("CNN Pooling", ["pooling layer"]),
    ("Max Pooling", ["maximum pooling"]),
    ("Average Pooling", ["average pooling"]),
    ("Recurrent Neural Network", ["RNN"]),
    ("Long Short Term Memory", ["LSTM"]),
    ("Gated Recurrent Unit", ["GRU"]),
    ("Bidirectional Neural Network", ["bidirectional RNN"]),
    ("Generative Adversarial Network", ["GAN"]),
    ("Generator Network", ["GAN generator"]),
    ("Discriminator Network", ["GAN discriminator"]),
    ("Transformer Neural Network", ["transformer architecture"]),
    ("Attention Mechanism", ["attention"]),
    ("Self Attention", ["self-attention"]),
    ("Embedding", ["vector embedding"]),
    ("Deep Reinforcement Learning", ["deep RL"]),

    # ========================================================
    # NATURAL LANGUAGE PROCESSING
    # ========================================================

    ("Natural Language Processing", ["NLP"]),
    ("Natural Language Understanding", ["NLU"]),
    ("Natural Language Generation", ["NLG"]),
    ("Text Processing", ["text preprocessing"]),
    ("Tokenization", ["text tokenization"]),
    ("Sentence Tokenization", ["sentence segmentation"]),
    ("Stemming", ["word stemming"]),
    ("Lemmatization", ["lemmatization"]),
    ("Stop Word Removal", ["stopword removal"]),
    ("Part of Speech Tagging", ["POS tagging"]),
    ("Named Entity Recognition", ["NER"]),
    ("Sentiment Analysis", ["sentiment classification"]),
    ("Text Classification", ["document classification"]),
    ("Text Similarity", ["semantic similarity"]),
    ("Information Retrieval", ["IR"]),
    ("Question Answering", ["QA systems"]),
    ("Text Summarization", ["automatic summarization"]),
    ("Machine Translation", ["automatic translation"]),
    ("Language Model", ["language modeling"]),
    ("Word Embedding", ["word vectors"]),
    ("Word2Vec", ["word2vec embeddings"]),
    ("GloVe", ["GloVe embeddings"]),
    ("TF IDF", ["TF-IDF"]),
    ("Cosine Similarity", ["cosine similarity NLP"]),
    ("Sentence Embedding", ["sentence embeddings"]),

    # ========================================================
    # LARGE LANGUAGE MODELS
    # ========================================================

    ("Large Language Model", ["LLM"]),
    ("Generative AI", ["generative artificial intelligence"]),
    ("Generative Model", ["generative machine learning"]),
    ("Foundation Model", ["foundation AI model"]),
    ("Pretrained Model", ["pre-trained model"]),
    ("Fine Tuning", ["model fine-tuning"]),
    ("Prompt", ["AI prompt"]),
    ("Prompt Engineering", ["prompt design"]),
    ("Context Window", ["LLM context window"]),
    ("Token", ["language model token"]),
    ("Transformer", ["transformer model"]),
    ("Attention Layer", ["transformer attention"]),
    ("Retrieval Augmented Generation", ["RAG"]),
    ("Knowledge Grounding", ["grounded AI"]),
    ("AI Hallucination", ["LLM hallucination"]),
    ("AI Evaluation", ["generative AI evaluation"]),
    ("AI Safety", ["artificial intelligence safety"]),

    # ========================================================
    # COMPUTER VISION
    # ========================================================

    ("Computer Vision", ["CV"]),
    ("Image Processing", ["digital image processing"]),
    ("Image Classification", ["visual classification"]),
    ("Object Detection", ["object recognition"]),
    ("Image Segmentation", ["semantic segmentation"]),
    ("Instance Segmentation", ["instance image segmentation"]),
    ("Face Recognition", ["facial recognition"]),
    ("Optical Character Recognition", ["OCR"]),
    ("Image Feature", ["visual features"]),
    ("Edge Detection", ["image edge detection"]),
    ("Image Filtering", ["image filters"]),
    ("Image Augmentation", ["data augmentation images"]),
    ("Convolution", ["image convolution"]),
    ("Computer Vision Model", ["vision model"]),

    # ========================================================
    # REINFORCEMENT LEARNING
    # ========================================================

    ("Reinforcement Learning Agent", ["RL agent"]),
    ("Reinforcement Learning Environment", ["RL environment"]),
    ("State in Reinforcement Learning", ["RL state"]),
    ("Action in Reinforcement Learning", ["RL action"]),
    ("Reward", ["reinforcement reward"]),
    ("Policy", ["RL policy"]),
    ("Value Function", ["state value"]),
    ("Q Function", ["Q-value"]),
    ("Q Learning", ["Q-learning"]),
    ("Deep Q Network", ["DQN"]),
    ("Exploration", ["exploration RL"]),
    ("Exploitation", ["exploitation RL"]),
    ("Exploration Exploitation Tradeoff", ["exploration-exploitation"]),

    # ========================================================
    # RECOMMENDER SYSTEMS
    # ========================================================

    ("Recommendation System", ["recommender system"]),
    ("Content Based Recommendation", ["content-based filtering"]),
    ("Collaborative Filtering", ["collaborative recommendation"]),
    ("User Based Collaborative Filtering", ["user-based filtering"]),
    ("Item Based Collaborative Filtering", ["item-based filtering"]),
    ("Hybrid Recommendation System", ["hybrid recommender"]),
    ("Recommendation Ranking", ["recommendation ranking"]),
    ("Recommendation Evaluation", ["recommender evaluation"]),

    # ========================================================
    # AI DATA AND TRAINING
    # ========================================================

    ("Data Preprocessing for Machine Learning", ["ML preprocessing"]),
    ("Data Cleaning for Machine Learning", ["ML data cleaning"]),
    ("Data Augmentation", ["training data augmentation"]),
    ("Synthetic Data", ["synthetic training data"]),
    ("Training Pipeline", ["ML training pipeline"]),
    ("Model Pipeline", ["machine learning pipeline"]),
    ("Hyperparameter", ["ML hyperparameter"]),
    ("Hyperparameter Tuning", ["model tuning"]),
    ("Grid Search", ["grid search hyperparameters"]),
    ("Random Search", ["randomized search"]),
    ("Early Stopping", ["early stopping training"]),
    ("Regularization", ["ML regularization"]),
    ("L1 Regularization", ["L1 penalty"]),
    ("L2 Regularization", ["L2 penalty"]),
    ("Dropout", ["neural network dropout"]),

    # ========================================================
    # AI FAIRNESS AND ETHICS
    # ========================================================

    ("AI Bias", ["artificial intelligence bias"]),
    ("Algorithmic Bias", ["algorithm bias"]),
    ("Dataset Bias", ["training data bias"]),
    ("Fairness in AI", ["AI fairness"]),
    ("Algorithmic Fairness", ["fair machine learning"]),
    ("AI Transparency", ["transparent AI"]),
    ("AI Accountability", ["responsible AI accountability"]),
    ("AI Privacy", ["privacy in artificial intelligence"]),
    ("AI Governance", ["AI governance"]),
    ("Human in the Loop", ["human oversight"]),
    ("AI Reliability", ["reliable AI"]),
    ("AI Robustness", ["robust AI"]),
    ("Adversarial Example", ["adversarial machine learning"]),
    ("Adversarial Machine Learning", ["adversarial attacks on ML"]),
]


# ============================================================
# GENERATOR
# ============================================================

def generate() -> list[dict]:
    """Generate the Artificial Intelligence and Machine Learning
    knowledge family.
    """

    records = []

    for topic, aliases in CONCEPTS:

        records.extend(
            build_knowledge_family(
                topic=topic,
                category=CATEGORY,
                aliases=aliases,
                education_level="university",
                difficulty="intermediate",
            )
        )

    return records


# ============================================================
# DIRECT EXECUTION
# ============================================================

if __name__ == "__main__":

    records = generate()

    print("=" * 60)
    print("AI / MACHINE LEARNING GENERATOR")
    print("=" * 60)
    print(f"Concepts : {len(CONCEPTS)}")
    print(f"Records  : {len(records)}")
    print("=" * 60)