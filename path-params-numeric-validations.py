from fastapi import FastAPI, Path, Query

from typing import Annotated


app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    size: Annotated[float, Query(gt=0, lt=10.5)],
    item_id: Annotated[
      int, Path(title="The ID of the item to get", ge=1, gt=0, le=1000)
    ],
    q: Annotated[str | None, Query(alias="item-query")] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if size:
        results.update({"size": size})
    return results

'''
gt: hacha greatort
ge: gmayor que o ecual
lt: less than
le: lmenos que o ecual
'''