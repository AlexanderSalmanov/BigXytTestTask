from flask import jsonify
from extensions import db


class CRUDMixin:
    __table_args__ = {'extend_existing': True}
    
    id = db.Column(db.Integer, primary_key=True)
    
    @classmethod
    def get_by_id(cls, id: int):
        return cls.query.get(id)
    
    @classmethod
    def create(cls, **kwargs):
        instance = cls(**kwargs)
        return instance.save()
    
    def _update(self, commit=True, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        return commit and self.save(commit=commit) or self
    
    def update(self, commit=True, **kwargs):
        return self._update(commit, **kwargs)
    
    def save(self, commit=True):
        db.session.add(self)
        if commit:
            db.session.commit()
        return self
    
    def delete(self, commit=True):
        db.session.delete(self)
        return commit and db.session.commit()


def to_success_response(data = dict(), status_code: int = 200):
    return jsonify({'results': data}), status_code

    
def to_error_response(data = dict(), status_code: int = 400) -> tuple[dict, int]:
    return jsonify({'error': data}), status_code
    
    
    