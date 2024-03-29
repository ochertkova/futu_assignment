def fav_languages(user):
    """Collect language flag from all user's repositories,
       build frequency list, and return 3 most frequent languages
    """
    fav_lang_dict = {}
    if user:
        for r in user['repos']:
            if r['language'] not in fav_lang_dict:
                fav_lang_dict[r['language']] = 0
            fav_lang_dict[r['language']] += 1
    fav_lang_list = [{ 'name': name, 'freq': freq } for (name, freq) in fav_lang_dict.items() if name != None]
    fav_lang_list_sorted = sorted(fav_lang_list,key = lambda x: x['freq'],reverse=True)
    return fav_lang_list_sorted[:3]


    

