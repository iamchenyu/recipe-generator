from app import app
from models import db, Diet

with app.app_context():
    db.drop_all()
    db.create_all()

gluten_free = Diet(diet_label="gluten free")
ketogenic = Diet(diet_label="ketogenic")
vegetarian = Diet(diet_label="vegetarian")
lacto_vegetarian = Diet(diet_label="lacto vegetarian")
ovo_vegetarian = Diet(diet_label="ovo vegetarian")
lacto_ovo_vegetarian = Diet(diet_label="lacto ovo vegetarian")
vegan = Diet(diet_label="vegan")
pescetarian = Diet(diet_label="pescetarian")
paleo = Diet(diet_label="paleolithic")
primal = Diet(diet_label="primal")
low_FODMAP = Diet(diet_label="low Fodmap")
whole30 = Diet(diet_label="whole30")
dairy_free = Diet(diet_label="dairy free")

with app.app_context():
    db.session.add_all([gluten_free, ketogenic, vegetarian,
                        lacto_vegetarian, ovo_vegetarian, lacto_ovo_vegetarian, vegan, pescetarian, paleo, primal, low_FODMAP, whole30, dairy_free])
    db.session.commit()
