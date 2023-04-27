def get_fields(model_class, excluded_fields=['id', 'date_created', 'date_updated']):
    """ get the fields of a model class and
        extract the names.
    """
    def __extract(fields):
        for f in fields:
            if f.name in excluded_fields: continue
            yield f.name

    return list(__extract(model_class._meta.fields))