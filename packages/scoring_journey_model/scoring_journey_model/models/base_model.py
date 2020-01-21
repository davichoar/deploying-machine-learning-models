
class BaseModel:
    """Base model with basic functions"""
    def __init__(self, features, target):
        """
        Create a new base model.

        Input:
            features [str]: List of feature names.
        """
        self.features = features
        self.target = target

    def train_all(self, df_train):
        """
        Train the model (and all submodels) on the given data.

        Args:
             df_train (DataFrame): Training data as pandas dataframe. The
                dataframe needs columns for all features and targets.

        Effect:
            This model will have a reference to the trained (sub)models.
        """
        pass

    def predict(self, df_test):
        """
        Make predictions for a full dataframe.

        Args:
            df_test (DataFrame): Test data as pandas dataframe. The dataframe
            needs columns for all the features.

        Returns:
            predictions for all the rows in the dataframe as a numpy array
            (order is kept).
        """
        pass

    def supports(self, category, country, sku):
        """
        Check if this model supports the given category, country, sku
        combination.

        Args:
            category (str): Product category represented as string.
            country (str): Country represented as string.
            sku (str): SKU represented as string.

        Returns:
            True iff this model supports the given categoruy, country & sku.
        """
        pass

    def get_model(self, category, country, sku):
        """
        Return a model that is able to make predictions for the given parameters

        Args:
            category (str): Product category represented as string.
            country (str): Country represented as string.
            sku (str): SKU represented as string.

        Returns:
            (Estimator): A model that is able to make predictions for the given
                category, country, sku.
        """
        pass
