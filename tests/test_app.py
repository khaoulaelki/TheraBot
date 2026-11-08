
import importlib
import sys
import types

import pytest


@pytest.fixture
def client(monkeypatch):
    # Simulate the chatbot module to avoid loading the AI model
    fake_chatbot = types.ModuleType("chatbot")

    def fake_chat_with_bot(user_input, chat_history_ids=None):
        return "Mock chatbot response", None

    fake_chatbot.chat_with_bot = fake_chat_with_bot

    monkeypatch.setitem(sys.modules, "chatbot", fake_chatbot)
    sys.modules.pop("app", None)

    app_module = importlib.import_module("app")
    app_module.app.config["TESTING"] = True
    app_module.chat_history_ids = None

    yield app_module.app.test_client()

    sys.modules.pop("app", None)


def test_stress_message(client):
    response = client.post(
        "/chat",
        json={"message": "I feel stressed"}
    )

    assert response.status_code == 200
    assert "stressed" in response.json["reply"]


def test_default_chatbot_response(client):
    response = client.post(
        "/chat",
        json={"message": "Hello"}
    )

    assert response.status_code == 200
    assert response.json["reply"] == "Mock chatbot response"
