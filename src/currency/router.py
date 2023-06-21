from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from database.engine import get_async_session
from .service import currency_by_name, all_currencies, currency_by_name_and_data

currency_router = APIRouter(prefix="/rates", tags=['Rates'])


@currency_router.get("/{name}", name='currency')
async def currency(
    name,
    session: AsyncSession = Depends(get_async_session)
):
    currency = await currency_by_name(name, session)
    return {currency[0].abbreviation: currency[0].rates[0].course}

@currency_router.get("/", name='currencies')
async def currency(
    session: AsyncSession = Depends(get_async_session)
):
    currencies = await all_currencies(session)
    return currencies

@currency_router.get("/{name}/{data}", name='currencies')
async def currency(
    name,
    data,
    session: AsyncSession = Depends(get_async_session)
):
    currencies = await currency_by_name_and_data(name, data, session)
    return currencies
