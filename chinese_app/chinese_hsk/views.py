from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import TextFull, TextTitle, TextMeta, TextParagraph
import jieba
import re
import random


# Create your views here.
def index(request):
    return render(request, "chinese_hsk/index.html")
def hsk_texts(request, hsk_level):
    # Fetch texts corresponding to the selected HSK level
    texts = TextMeta.objects.filter(hsk_level=hsk_level).select_related('texttitle') 
    context = {
        'texts': texts,
        'hsk_level': hsk_level,
    }
    return render(request, 'chinese_hsk/hsk_texts.html', context)

def excercises(request):
    return render(request, "chinese_hsk/excercises.html")

def text_detail(request, text_id):
    text_meta = get_object_or_404(TextMeta, text_id=text_id)  # Using get_object_or_404 for better practice
    text_full = get_object_or_404(TextFull, text_id=text_meta)  # Get TextFull using the TextMeta instance
    text_title = get_object_or_404(TextTitle, text_id=text_meta)  # Get TextTitle using the TextMeta instance

    context = {
        'text_full': text_full.text_full,
        'text_title': text_title.text_name,
    }
    return render(request, 'chinese_hsk/text_detail.html', context)

def paragraph_blankedeasy(request, text_id=6, p_number=5):
    # Fetch the specific paragraph using text_id and p_number
    paragraph = get_object_or_404(TextParagraph, text_id=text_id, p_number=p_number)

    # Split paragraph and select random segment
    pattern = r'[，。？！：；、—]'
    segments = re.split(pattern, paragraph.p_text)
    segments = [segment.strip() for segment in segments if segment.strip()]
    random_segment = random.choice(segments)

    # Create a blanked-out version of the paragraph
    paragraph_blanked = paragraph.p_text.replace(random_segment, '___________')
    segment_words = list(jieba.cut(random_segment))
    random.shuffle(segment_words)
    

    

    context = {
        'paragraph_blanked': paragraph_blanked,
        'segment_words': segment_words,
        'random_segment': random_segment,
    }
    return render(request, 'chinese_hsk/paragraph_blankedeasy.html', context)
#views.py
