import os
import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_api_equipos():
    """Valida que el endpoint del árbol de equipos responda correctamente"""
    response = client.get("/api/equipos")
    assert response.status_code == 200
    data = response.json()
    # Debe retornar el JSON del árbol o el mensaje controlado si no existe el archivo
    assert "divisiones" in data or "error" in data

def test_api_registros():
    """Valida que el endpoint de registros devuelva la estructura adecuada"""
    response = client.get("/api/registros")
    assert response.status_code == 200
    data = response.json()
    assert "canibalizaciones" in data
    assert isinstance(data["canibalizaciones"], list)
