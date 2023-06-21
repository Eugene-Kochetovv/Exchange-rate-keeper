from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import load_only, selectinload, join
from sqlalchemy import insert

from database.models import Currency, Rates

from database.engine import async_session_maker

from datetime import datetime

async def save_currencies(currencies):
    date = datetime.now()
    async with async_session_maker() as session:
        for currency in currencies.items():
            stmt = insert(Rates).values(
                currency_abb = currency[0],
                course = float(currency[1]["USD"]),
                date = date.date(),
                time = date.time()
                )
            r = await session.execute(stmt)

        await session.commit()
        return True

async def new_currencies(currencies):
    async with async_session_maker() as session:
        for currency in currencies:
            stmt = insert(Currency).values(abbreviation = currency)
            r = await session.execute(stmt)

        await session.commit()
        return True


async def currency_by_name(name, session):
    stmt = select(Currency).where(Currency.abbreviation == name).options(load_only(Currency.abbreviation).selectinload(Currency.rates).options(load_only(Rates.course)))
    r = await session.execute(stmt)
    return r.scalars().all()


async def all_currencies(session):
    stmt = select(Currency).options(load_only(Currency.abbreviation), selectinload(Currency.rates).options(load_only(Rates.course, Rates.date, Rates.time)))
    r = await session.execute(stmt)
    return r.scalars().all()

async def currency_by_name_and_data(name, data, session):
    t = datetime.strptime(data,'%Y-%m-%d').date()
    stmt = select(Currency).where(Currency.abbreviation == name).options(load_only(Currency.abbreviation)).options(selectinload(Currency.rates).load_only(Rates.course, Rates.time))
    r = await session.execute(stmt)
    return r.scalars().all()
