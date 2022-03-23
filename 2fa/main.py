from apscheduler.schedulers.background import BackgroundScheduler
from app import app
from models import db, Token
import views


def del_all_tokens():
    db.session.query(Token).delete()
    db.session.commit()
    return


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(del_all_tokens, trigger='interval', seconds=86400)
    scheduler.start()
    app.run()