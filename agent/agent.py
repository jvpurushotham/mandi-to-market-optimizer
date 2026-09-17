from agent.ai_router import run_ai_query
from agent.final_answer import generate_final_answer
from agent.charts import create_chart


def ask_agent(query):
    result = run_ai_query(query)

    understanding = result["understanding"]
    data = result["data"]
    intent = understanding.get("intent")

    if intent == "unknown":
        return {
            "answer": (
                "I can answer questions about mandi arrivals, "
                "crop prices, MSP, transport, warehouses, and weather "
                "from the available agricultural dataset."
            ),
            "intent": "unknown",
            "data": None,
            "chart": None,
        }

    answer = generate_final_answer(
        query,
        understanding,
        data,
    )

    chart = create_chart(intent, data)

    return {
        "answer": answer,
        "intent": intent,
        "data": data,
        "chart": chart,
    }