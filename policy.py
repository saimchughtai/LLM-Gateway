from detector import detect_injection
from presidio_ext import detect_pii


def policy_engine(prompt):

    injection_score = detect_injection(prompt)
    pii_results = detect_pii(prompt)

    if injection_score >= 1:
        return "BLOCK"

    if len(pii_results) > 0:
        return "MASK"

    return "ALLOW"