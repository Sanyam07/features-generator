import abc

class FeatureGenerationStrategyAbstract(object):
    """Provides abstraction for features generation"""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def generate(self, df, colname1, colname2):
        """Required Method"""

    @abc.abstractmethod
    def featurename(self, colname1, colname2):
        """Required Method"""

    @abc.abstractmethod
    def equivalent_featurenames(self, colname1, colname2):
        """Required Method. Used to reflect commutativity."""

class SumFeatureGenerationStrategy(FeatureGenerationStrategyAbstract):
    def generate(self, df, colname1, colname2):
        return df[featurename(colname1, colname2)]=df[colname1]+df[colname2]

    def featurename(self, colname1, colname2):
        return "{}_sum_{}".format(colname1, colname2)

    def equivalent_featurenames(self, colname1, colname2):
        return [featurename(colname1, colname2), featurename(colname2, colname1)]


class DiffFeatureGenerationStrategy(FeatureGenerationStrategyAbstract):
    def generate(self, df, colname1, colname2):
        return df[featurename(colname1, colname2)]=df[colname1]-df[colname2]

    def featurename(self, colname1, colname2):
        return "{}_diff_{}".format(colname1, colname2)

    def equivalent_featurenames(self, colname1, colname2):
        return [featurename(colname1, colname2)]

class ProdFeatureGenerationStrategy(FeatureGenerationStrategyAbstract):
    def generate(self, df, colname1, colname2):
        return df[featurename(colname1, colname2)]=df[colname1]*df[colname2]

    def featurename(self, colname1, colname2):
        return "{}_prod_{}".format(colname1, colname2)

    def equivalent_featurenames(self, colname1, colname2):
        return [featurename(colname1, colname2), featurename(colname2, colname1)]

class DivFeatureGenerationStrategy(FeatureGenerationStrategyAbstract):
    def generate(self, df, colname1, colname2):
        return df[featurename(colname1, colname2)]=df[colname1]/df[colname2]

    def featurename(self, colname1, colname2):
        return "{}_div_{}".format(colname1, colname2)

    def equivalent_featurenames(self, colname1, colname2):
        return [featurename(colname1, colname2)]