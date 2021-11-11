from flask import Flask, render_template
from .models import DB, User, Tweet
from .twitter import add_or_update_user, get_all_usernames

# Factory function
def create_app():

    # Initializes app
    app = Flask(__name__)

    # Database configurations
    app.config['SQLAlchemy_DATABASE_URI'] = 'sqlit:///db.sqlite3'
    app.config['SQLAlchemy_TRACK_MODIFICATIONS'] = False

    # Give APP access to DB
    DB.init_app(app)

    # Listen to a 'route'
    # '/' is the home page route
    @app.route('/')
    def root():
        # Query the DB for all user
        users = User.query.all()
        # What I want to happen when somebody goes to the home page
        return render_template('base.html', title='Home', users=users)

    @app.route('/update')
    def update():
        '''updates all users'''
        usernames = get_all_usernames()
        for username in usernames:
            add_or_update_user(username)
        return 'updated'

    app_title = 'Twitoff DS32'

    @app.route('/test')
    def test():
        return f'A page from {app_title} app'

    @app.route('/populate')
    def populate():
        ryan = User(id=1, username='Ryan')
        DB.session.add(ryan)
        julian = User(id=2, username='Julian')
        DB.session.add(julian)
        tweet1 = Tweet(id=1, text='tweet text', user=ryan)
        DB.session.add(tweet1)
        tweet2 = Tweet(id=2, text="julian's tweet", user=julian)
        DB.session.add(tweet2)
        # save the database
        DB.session.commit()
        return "populate"
        
    @app.route('/reset')
    def reset():
        # remove everything from the database
        DB.drop_all()
        # Creates the database file initially.
        DB.create_all()
        return "reset"


    return app