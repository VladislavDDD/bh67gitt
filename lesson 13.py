from datetime import datetime
from typing import Optional, List, Type

from sqlalchemy import Column, INT, VARCHAR, TIMESTAMP, ForeignKey, TEXT, BOOLEAN, create_engine, DECIMAL
from sqlalchemy.orm import DeclarativeBase, declared_attr, sessionmaker, relationship
from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql.functions import count
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


class Base(DeclarativeBase):

    id = Column(INT, primary_key=True)

    engine = create_engine('postgresql://belhard:belhard@0.0.0.0:5432/belhard')
    session = sessionmaker(bind=engine)

    @declared_attr
    def __tablename__(cls):
        return ''.join(f'_{i.lower()}' if i.isupper() else i for i in cls.__name__).strip('_')


class Category(Base):
    name = Column(VARCHAR(64), unique=True, nullable=False, index=True)

    posts = relationship('Post', back_populates='category')


class Post(Base):
    title = Column(VARCHAR(128), nullable=False)
    description = Column(TEXT, nullable=False)
    date_publish = Column(TIMESTAMP, default=datetime.now())
    category_id = Column(INT, ForeignKey('category.id', ondelete='CASCADE'), nullable=False)
    is_published = Column(BOOLEAN, default=False)

    category = relationship('Category', back_populates='posts')

# with Category.session() as session:
#     categories = [
#         Category(name='Finance'),
#         Category(name='Sport'),
#     ]
#     session.add_all(categories)
#     try:
#         session.commit()
#     except IntegrityError:
#         pass
#     for category in categories:
#         session.refresh(category)
#
#     for category in categories:
#         print(category.id, category.name)

# with Category.session() as session:
#     category_1 = session.get(Category, 1)
#     print(category_1.id, category_1.name)
    # category_1.name = 'Politics'
    # session.add(category_1)
    # session.commit()

from sqlalchemy import select, update, delete, or_, and_, any_, all_


# with Category.session() as session:
#     # category = session.get(Category, 2)
#     # session.delete(category)
#     # session.commit()
#     # session.execute(
#     #     delete(Category)
#     #     .filter(Category.id >= 2)
#     # )
#     # session.commit()
#     # session.execute(
#     #     update(Category)
#     #     .values(name='Финансы')
#     #     .filter(Category.id == 2)
#     # )
#     # session.commit()
#     # obj = session.get(Category, 2)
#     # print(obj.name)
#     # objs = session.execute()  # список кортежей с экземплярами класса
#     # objs = session.scalars()  # список экземпляров класса
#     # objs = session.scalar()  # экземпляр класса (1 объект)
#     # objs = session.scalars(
#     #     select(Category)
#     #     .order_by(Category.name.desc())
#     #     .limit(2)
#     #     .offset(0)
#     # )
#     # print(objs.all())
#     # objs = session.execute(
#     #     select(Category, Post)
#     #     .join(Post, full=True)
#     # )
#     # print([obj for obj in objs])
#     # cat = session.get(Category, 1)
#     # print(cat.posts)
#     # post = Post(
#     #     title='Post1',
#     #     description='Description1',
#     #     category_id=1
#     # )
#     # session.add(post)
#     # session.commit()
#     # session.refresh(post)
#     # print(post.category.posts)
#     categories = session.scalars(select(Category))
#     for category in categories:
#         print(category.posts)


from pydantic import BaseModel, Field, ValidationError, validator


class PostSchema(BaseModel):
    title: str
    description: str
    date_publish: datetime
    is_published: bool
    category_id: int

    @validator('category_id', pre=True)
    def validate_category_id(cls, value: int) -> int:
        with Category.session() as session:
            obj = session.get(Category, value)
            if not obj:
                raise ValueError('category not found')
            return value

    class Config:
        orm_mode = True


class CategorySchema(BaseModel):
    id: Optional[int]
    name: str = Field(max_length=64)
    posts: Optional[List[PostSchema]]

    class Config:
        orm_mode = True


with Category.session() as session:
    obj = session.get(Category, 1)
    # posts = [post.__dict__ for post in obj.posts]
    # data = obj.__dict__
    # data['posts'] = posts
    # schema = CategorySchema(**data)

    # print(schema)
    # print(schema)
    schema = CategorySchema.from_orm(obj)


# TODO Дан CSV файл с информацией о постах
#  необходимо данные из этого файла провалидировать через Pydantic
#  валидные данные записать в БД с использованием алхимии
#  невалидные данные записать в другой csv файл

from csv import DictReader, DictWriter
# with (
#     open('posts.csv', 'r', encoding='utf-8') as file,
#     open('invalid_posts.csv', 'w', encoding='utf-8') as out_file,
#     Category.session() as session
# ):
#     reader = DictReader(file)
#     writer = DictWriter(out_file, fieldnames=('title','description','date_publish','is_published','category_id'))
#     writer.writeheader()
#     for data in reader:
#         data: dict
#         try:
#             schema = PostSchema(**data)
#         except ValidationError:
#             writer.writerow(data)
#         else:
#             post = Post(**schema.dict())
#             session.add(post)
#             try:
#                 session.commit()
#             except IntegrityError:
#                 writer.writerow(data)

# TODO Выгрузить информацию постов в файл CSV\
# with (
#     open('posts_new.csv', 'w', encoding='utf-8') as file,
#     Category.session() as session
# ):
#     writer = DictWriter(file, fieldnames=('id', 'title','description','date_publish','is_published','category_id'))
#     posts = session.scalars(select(Post))
#     data = []
#     for post in posts:
#         post = post.__dict__
#         del post['_sa_instance_state']
#         post['id'] = str(post['id'])
#         post['category_id'] = str(post['category_id'])
#         post['date_publish'] = post['date_publish'].isoformat()
#         post['is_published'] = str(int(post['is_published']))
#         data.append(post)
#     writer.writeheader()
#     writer.writerows(data)


with Category.session() as session:
    objs = session.scalar(
        select(count(Category.id))
    )
    print(objs)