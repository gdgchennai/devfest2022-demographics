lookup_set = {
    'VIT Chennai': ['vit', 'vellore', 'gdsc vit'],
    'SRM IST': ['srm', 'gdsc srm'],
    'CIT': ['cit', 'chennai institite', 'gdsc cit', 'citc'],
    'Saveetha': ['saveetha', 'sec'],
    'HITS': ['hits', 'gdsc hits', 'hindustan'],
    'KCG': ['kcg', 'kcg college of technology', 'kcg tech'],
    'Chennai': ['chennai'],
    'Vellore': ['vellore'],
    'Coimbatore': ['coimbatore', 'covai', 'kovai'],
    'Bengaluru': ['bengaluru', 'bangalore'],
    'Thiruvallur': ['thiruvallur', 'tiruvallur', 'trivallur', 'thiruvalur', 'tiruvalur', 'trivalur', 'thiruvaloor', 'tiruvaloor', 'trivaloor'],
}


def normalize(value):
    for key, values in lookup_set.items():
        for match_item in values:
            # A very hacky lookup. Not the right way. Don't even think about it.
            # Just shamelessly using it just because I am lazy.
            if value.lower().startswith(match_item) or value.lower().endswith(match_item) or match_item in value.lower():
                return key
    return value
