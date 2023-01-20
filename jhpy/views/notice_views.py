from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Notice

def notice(request):
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    notice_list = Notice.objects.order_by('-create_date')
    if kw:
        notice_list = notice_list.filter(
            Q(subject__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw) |  # 내용 검색
            Q(answer__content__icontains=kw) |  # 답변 내용 검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이 검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이 검색
        ).distinct()
    paginator = Paginator(notice_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'notice_list': page_obj, 'page': page, 'kw': kw}
    return render(request, 'jhpy/main.html', context)

def notice_detail(request, notice_id):
    notice = Notice.objects.get(id=notice_id)
    context = {'notice': notice}
    return render(request, 'jhpy/notice_detail.html', context)
