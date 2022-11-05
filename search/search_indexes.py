from haystack import indexes

class EpisodeIndex(indexes.SearchIndex, indexes.Indexable):

    themes = indexes.CharField(document=True)
    episode_title = indexes.CharField(model_attr='Episode Title')
    alex_says = indexes.CharField(model_attr='Alex says')
    deep_dive_topic = indexes.CharField(model_attr='Deep Dive Topic')
    deep_dive_aliases = indexes.CharField(model_attr='Aliases')
    people = indexes.CharField(model_attr='People')