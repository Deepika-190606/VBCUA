from sentence_transformers import SentenceTransformer
from sentence_transformers import util

model = SentenceTransformer("all-MiniLM-L6-v2")

def compare_text(reference_text, student_text):

    reference_embedding = model.encode(reference_text, convert_to_tensor=True)

    student_embedding = model.encode(student_text, convert_to_tensor=True)

    similarity = util.cos_sim(reference_embedding, student_embedding)

    return similarity.item()

def understanding_level(score):

    if score >= 0.90:
        return "🟢 Excellent Understanding"

    elif score >= 0.75:
        return "🟡 Good Understanding"

    elif score >= 0.55:
        return "🟠 Moderate Understanding"

    else:
        return "🔴 Poor Understanding"