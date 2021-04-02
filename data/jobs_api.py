import flask
from flask import jsonify, request

from . import db_session
from .jobs import Jobs

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return flask.jsonify({'jobs': [item.to_dict(
        only=('id', 'job', 'team_leader', 'work_size', 'collaborators',
              'start_date', 'end_date', 'is_finished')
    )
        for item in jobs]})
