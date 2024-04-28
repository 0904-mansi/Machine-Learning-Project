from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for comments (replace with actual API calls)
comments = [
    {
        "at": "2023-01-15",
        "author": "Fredrick Johnson",
        "like": 3,
        "reply": 1,
        "text": "Economic growth is essential for any nation."
    },
    {
        "at": "2023-01-20",
        "author": "Alice Smith",
        "like": 6,
        "reply": 2,
        "text": "I agree with Fredrick's point."
    },
    # Add more comments here
]

@app.route('/search', methods=['GET'])
def search_comments():
    search_author = request.args.get('search_author')
    at_from = request.args.get('at_from')
    at_to = request.args.get('at_to')
    like_from = int(request.args.get('like_from', 0))
    like_to = int(request.args.get('like_to', float('inf')))
    reply_from = int(request.args.get('reply_from', 0))
    reply_to = int(request.args.get('reply_to', float('inf')))
    search_text = request.args.get('search_text')

    filtered_comments = []
    for comment in comments:
        if (not search_author or search_author.lower() in comment['author'].lower()) and \
           (not at_from or at_from <= comment['at'] <= at_to) and \
           (like_from <= comment['like'] <= like_to) and \
           (reply_from <= comment['reply'] <= reply_to) and \
           (not search_text or search_text.lower() in comment['text'].lower()):
            filtered_comments.append(comment)

    return jsonify(filtered_comments)

if __name__ == '__main__':
    app.run()
