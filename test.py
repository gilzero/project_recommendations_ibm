# make a recommendations for a user who only has interacted with article id '1427.0'

print(
    f"💡 \nSince you checked article 1427:\n "
    f"({_get_article_titles([1427])[0]}), \n"
    f"you might also be interested in these:\n")

recs_for_user_1427th_titles = make_content_recs(1427)[1]
for k, v in enumerate(recs_for_user_1427th_titles):
    print(k + 1, v)

