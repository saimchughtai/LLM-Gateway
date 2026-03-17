# LLM Security Mini Gateway

In order to defend LLM-based systems against adversarial attacks such as prompt injection, jailbreaking, system prompt extraction, and leaking of sensitive data, this project proposes a modular security gateway. Before any user input reaches the LLM backend, it is processed through a three-stage pipeline.

## Features
- Prompt Injection Detection
- Sensitive Data Detection
- Policy Decision Engine
- Lightweight Security Gateway

## Technologies
Python  
Microsoft Presidio  

## Installation
pip install -r requirements.txt

## Running the System
python main_gateway.py

## Project Structure
detector.py – detects prompt injection  
presidio_ext.py – detects sensitive information  
policy.py – security decision logic  
main_gateway.py – gateway execution script




