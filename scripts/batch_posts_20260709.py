#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-07-09 블로그 20편 일괄 생성"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POSTS_PATH = ROOT / "data" / "blog-posts.json"
DATE = "2026-07-09"

NEW_POSTS = [
    {
        "id": "parents-day-massage-gift-2026",
        "title": "어버이날 지난 뒤에도 통하는 효도 선물 — 마사지 기프트카드 후기형 가이드",
        "summary": "5월을 놓쳤어도 괜찮아요. 부모님 허리·무릎·어깨를 위한 마사지 기프트카드, 계절과 상관없이 통하는 효도 선물 고르는 법.",
        "category": "어버이·효도",
        "tags": ["효도선물", "부모님", "마사지기프트"],
        "emoji": "💐",
        "media": "warm",
        "content": """<p>어버이날 카네이션은 받으셨는데, 다음 날 허리 통증 이야기를 하시는 부모님—익숙한 풍경이죠. 7월, <strong>마사지 기프트카드</strong>는 \"늦은 효도\"가 아니라 \"지금 필요한 효도\"로 받아들여지는 경우가 많습니다.</p>
<h2>부모님이 거절할 때 대처법</h2>
<p>\"비싼 건 사지 마\"라고 하시는 분들께는 <strong>5~7만 원 60분 코스</strong>로 부담을 낮추세요. 저압·부드러운 스웨디시를 미리 요청하면 나이에 맞게 조절해 줍니다.</p>
<ul>
<li>무릎·허리가 불편하면 <strong>등·어깨 위주</strong> 코스 선택</li>
<li>혈압·당뇨 약 복용 중이면 예약 시 알리기</li>
<li>동행해 드리면 첫 방문 거부감이 줄어듭니다</li>
</ul>
<p>자세한 금액은 <a href="../posts/gift-for-parents-massage.html">부모님 선물 가이드</a>를 참고하세요.</p>
<h2>실물 vs 디지털, 부모님은 어떤 게 편할까</h2>
<p>스마트폰에 익숙하시면 디지털이, 손에 쥐는 카드를 좋아하시면 실물이 낫습니다. 디지털은 <strong>전화로 예약 방법</strong>을 함께 알려 드리는 게 핵심이에요.</p>
<h2>메시지 한 줄 예시</h2>
<p>\"꽃 대신 등·어깨 풀 시간 드릴게요. 편한 날 전화만 주세요.\"</p>
<div class="tip-box"><strong>팁</strong> 형제자매와 <strong>금액권을 나눠 충전</strong>하면 90분 프리미엄 코스도 부담 없이 가능합니다.</div>
<h2>이용 전 확인할 3가지</h2>
<ol>
<li>샵까지 이동 거리(15~20분 이내 권장)</li>
<li>계단·문턱 없는 매장인지</li>
<li>유효기간 12개월 이상</li>
</ol>""",
    },
    {
        "id": "teachers-day-wellness-gift",
        "title": "스승의 날·감사 선물 — 선생님·멘토에게 마사지 기프트카드 드리기",
        "summary": "편지와 함께 보내는 실용 힐링 선물. 학원·학교 선생님, 직장 멘토에게 통하는 마사지 기프트카드 금액·에티켓.",
        "category": "스승·감사",
        "tags": ["감사선물", "스승의날", "마사지기프트"],
        "emoji": "📚",
        "media": "gift",
        "content": """<p>말씀 한마디보다 오래 남는 선물을 찾을 때, <strong>마사지 기프트카드</strong>는 \"목·어깨 쉬어 가세요\"라는 메시지를 몸으로 전달합니다. 다만 관계에 따라 금액·전달 방식을 조절하는 센스가 필요해요.</p>
<h2>관계별 적정 금액</h2>
<table class="article-table">
<tr><th>대상</th><th>금액</th><th>비고</th></tr>
<tr><td>담임·학원 강사</td><td>3~5만 원</td><td>학부모 다수 참여 시 5~7만</td></tr>
<tr><td>대학 지도교수</td><td>7~10만 원</td><td>졸업·배출 감사</td></tr>
<tr><td>직장 멘토</td><td>5~10만 원</td><td>디지털 + 짧은 편지</td></tr>
</table>
<h2>에티켓 — 피해야 할 점</h2>
<ul>
<li>과도한 금액(부담·오해 소지)</li>
<li>특정 체인만 가능한 카드(거주지와 멀면)</li>
<li>현금 영수증·세금 관련 오해 없도록 공식 채널 구매</li>
</ul>
<p><a href="../posts/gift-card-amount-guide.html">금액 가이드</a>에서 표를 더 보실 수 있습니다.</p>
<h2>전달 문구</h2>
<p>\"가르침 감사합니다. 바쁜 일상, 잠시 몸부터 쉬어 가세요.\"</p>""",
    },
    {
        "id": "pregnancy-postpartum-gift-card",
        "title": "출산·임산부 선물 — 산후 마사지 기프트카드 고를 때 체크리스트",
        "summary": "임신 중·출산 후 받을 수 있는 마사지 기프트카드. 시기·코스·안전 수칙과 배우자가 준비하는 센스 있는 선물법.",
        "category": "출산·임산부",
        "tags": ["출산선물", "임산부", "산후케어"],
        "emoji": "👶",
        "media": "nature",
        "content": """<p>출산 선물로 기저귀·젖병이 쌓일 때, <strong>산후 회복용 마사지 기프트카드</strong>는 \"네 몸도 챙기자\"는 메시지로 큰 위로가 됩니다. 다만 임신·수유 시기에 따라 이용 가능 여부가 달라 <strong>사전 확인</strong>이 필수예요.</p>
<h2>시기별 이용 가이드</h2>
<ul>
<li><strong>임신 중</strong> — 산전 전문 코스만 가능, 의사·샵 상담 필수</li>
<li><strong>출산 후 6주~</strong> — 대부분 산후·전신 이완 코스 시작 (자연분만·제왕에 따라 다름)</li>
<li><strong>수유 중</strong> — 유두·복부 압력 약한 코스, 오일 성분 확인</li>
</ul>
<div class="warn-box"><strong>주의</strong> 의료 행위·치료 목적이 아닌 웰니스 마사지입니다. 몸 상태에 따라 이용 불가할 수 있으니 <strong>산부인과·전문의 상담</strong> 후 진행하세요.</div>
<h2>배우자·지인이 준비하는 법</h2>
<p>출산 전 <strong>디지털 카드</strong>를 보내 두고, \"출산 후 2~3개월 뒤 쓰면 돼\"라고 적어 두면 부담이 줄어요. <a href="../posts/digital-gift-card-tips.html">디지털 발송</a> 참고.</p>
<h2>추천 금액</h2>
<p>친한 지인 7~10만 원, 배우자가 주는 선물 10~15만 원(90분 산후·림프). <a href="../posts/birthday-wellness-gift.html">생일·웰니스 선물</a> 금액표도 참고하세요.</p>""",
    },
    {
        "id": "working-mom-gift-card-guide",
        "title": "워킹맘·육아맘에게 보내는 마사지 기프트카드 — 시간 없는 엄마를 위한 선물",
        "summary": "육퇴 직전 60분, 등·목 집중 코스. 친구·남편·부모가 건네는 워킹맘 맞춤 기프트카드 실전 팁.",
        "category": "육아·워킹맘",
        "tags": ["워킹맘", "육아", "선물"],
        "emoji": "👩‍👧",
        "media": "sunset",
        "content": """<p>\"엄마도 쉬어야지\"—말은 쉽지만 시간이 없죠. <strong>미리 결제된 마사지 기프트카드</strong>는 \"아깝다\"는 마음이 예약을 만들어 냅니다. 7월, 여름 방학·아이 캠프 시즌이 워킹맘에게는 유일한 시간 창이 될 수 있어요.</p>
<h2>60분이면 충분한 이유</h2>
<p>90분은 부담, 30분은 아쉬움—<strong>60분 목·어깨·등</strong> 집중이 현실적입니다. 젖꼭지·유두 주변은 건드리지 않는 코스를 요청하세요.</p>
<h2>누가 선물하면 좋을까</h2>
<ul>
<li><strong>남편</strong> — 출산·육아 감사, 디지털 + \"이번 주 토요일 내가 아이 봐줄게\"</li>
<li><strong>친구</strong> — 5~7만 원, 집 근처 샵 추천 리스트 동봉</li>
<li><strong>친정·시댁</strong> — 10만 원, 부담 없는 금액·코스 설명서</li>
</ul>
<p><a href="../posts/self-care-gift-card.html">셀프케어 기프트카드</a> 글과 함께 읽어보세요.</p>
<h2>예약 팁</h2>
<ol>
<li>아이 하원·수업 시간에 맞춘 슬롯</li>
<li>샤워·대기 시간 포함해 90분 블록 잡기</li>
<li>취소 규정 확인(아이 갑작스런 발열 등)</li>
</ol>""",
    },
    {
        "id": "aroma-gift-card-scent-guide",
        "title": "아로마·향 테라피 기프트카드 — 향에 민감한 분께 고르는 법",
        "summary": "라벤더·유칼립·시트러스, 향 선택부터 알레르기·임신 주의까지. 아로마 마사지 기프트카드 선물 가이드.",
        "category": "아로마·향기",
        "tags": ["아로마", "향테라피", "마사지기프트"],
        "emoji": "🌿",
        "media": "nature",
        "content": """<p>아로마 마사지는 <strong>향</strong>이 경험의 절반입니다. 기프트카드를 살 때 \"아로마 60분\"만 적혀 있으면, 받는 분이 샵에서 처음 보는 오일을 맞닥뜨릴 수 있어요. 선물할 때 <strong>향 선택권</strong>을 함께 적어 주면 센스가 살아납니다.</p>
<h2>취향별 향 추천</h2>
<ul>
<li><strong>수면·이완</strong> — 라벤더, camomile 계열</li>
<li><strong>피로·활력</strong> — 로즈마리, 페퍼민트 (강한 향 싫어하면 피하기)</li>
<li><strong>스트레스</strong> — 베르가못, 일랑일랑</li>
</ul>
<h2>민감군 체크</h2>
<p>천식·향 알레르기·임신·수유 중에는 <strong>무향 또는 저자극</strong> 코스를 선택하세요. 샵에 \"오일 성분표\" 요청 가능.</p>
<h2>기프트카드 vs 코스 지정</h2>
<p>금액권이면 샵에서 아로마 업그레이드, 코스 지정형이면 \"아로마 90분\" 고정. <a href="../posts/gift-card-vs-coupon.html">기프트카드 vs 쿠폰</a> 비교 참고.</p>
<div class="tip-box"><strong>팁</strong> \"향 선택은 현장에서, 부담되면 무향 말해 달라\"고 메모하면 완벽합니다.</div>""",
    },
    {
        "id": "sports-recovery-gift-card",
        "title": "운동·마라톤 후 회복 선물 — 스포츠 마사지 기프트카드 가이드",
        "summary": "헬스·러닝·등산 애호가에게. 대회·PT 후 근육 회복용 스포츠 마사지 기프트카드 금액·코스·타이밍.",
        "category": "스포츠·회복",
        "tags": ["스포츠마사지", "운동", "회복"],
        "emoji": "🏃",
        "media": "calm",
        "content": """<p>7월은 마라톤·트레일 대회가 많은 달입니다. 프로틴·폼롤러 대신 <strong>스포츠 마사지 기프트카드</strong>를 주면 \"다음 대회까지 몸 챙기자\"는 응원이 됩니다.</p>
<h2>언제 받으면 좋을까</h2>
<ul>
<li><strong>대회 다음 날</strong> — 가벼운 림프·플러시 (강한 딥티슈는 2~3일 후)</li>
<li><strong>주 1회 루틴</strong> — 60분 다리·허벅지 집중</li>
<li><strong>부상 회복 중</strong> — 의사·물리치료와 병행 여부 확인</li>
</ul>
<h2>코스 선택</h2>
<p>스포츠·딥티슈·스트레칭 결합 60~90분. 초보 운동인에게는 <strong>스웨디시 + 스트레칭</strong>이 부담 적습니다.</p>
<p>금액 7~10만 원. <a href="../posts/gift-card-amount-guide.html">금액 가이드</a> 참고.</p>
<h2>선물 메시지</h2>
<p>\"완주 축하! 종아리는 내가 맡을게—아니, 기프트카드가 맡을게.\"</p>""",
    },
    {
        "id": "thai-massage-gift-guide",
        "title": "타이 마사지 기프트카드 — 스트레칭·압력 취향별 선물 고르기",
        "summary": "타이·오일·발마사지 차이, 강한 압 싫어하는 분께는? 타이 마사지 기프트카드 입문·선물 가이드.",
        "category": "타이·스트레칭",
        "tags": ["타이마사지", "스트레칭", "마사지기프트"],
        "emoji": "🧘",
        "media": "gift",
        "content": """<p>타이 마사지는 <strong>스트레칭</strong>과 <strong>지압</strong>이 함께 옵니다. 처음 받는 분에게 타이 기프트카드를 주면 \"너무 아프지 않을까?\" 걱정이 앞서죠. 코스 이름만으로는 알기 어려워 <strong>선물 메모</strong>가 중요합니다.</p>
<h2>타이 vs 타이 오일 vs 발</h2>
<table class="article-table">
<tr><th>코스</th><th>특징</th><th>추천 대상</th></tr>
<tr><td>타이 전통</td><td>옷 입고, 스트레칭·지압</td><td>유연성·뻐근함</td></tr>
<tr><td>타이 오일</td><td>오일, 부드러운 압</td><td>타이 입문</td></tr>
<tr><td>발·다리</td><td>60분 집중</td><td>서·걷기 많은 직군</td></tr>
</table>
<h2>압력 조절 요청법</h2>
<p>\"soft pressure please\" 또는 \"약하게 부탁드려요\"—예약·현장 모두에서 말하면 됩니다.</p>
<p><a href="../posts/spa-vs-massage-gift.html">스파 vs 마사지샵</a> 비교도 도움이 됩니다.</p>""",
    },
    {
        "id": "swedish-massage-gift-intro",
        "title": "스웨디시 마사지 기프트카드 — 마사지 처음 받는 분께 가장 무난한 선물",
        "summary": "입문자·어르신·직장인 모두에게 통하는 스웨디시. 60분 vs 90분, 기프트카드로 고르는 기준.",
        "category": "스웨디·입문",
        "tags": ["스웨디시", "입문", "마사지기프트"],
        "emoji": "💆",
        "media": "calm",
        "content": """<p>\"마사지 한번도 안 받아 봤어\"—이 말을 들었을 때 가장 안전한 선택이 <strong>스웨디시 60분</strong>입니다. 기프트카드에 코스명까지 적혀 있으면 받는 분도 샵에서 고민이 줄어요.</p>
<h2>스웨디시가 입문에 좋은 이유</h2>
<ul>
<li>전신 오일, 익숙한 lying 포즈</li>
<li>압력 조절이 비교적 쉬움</li>
<li>대부분 샵의 기본 메뉴</li>
</ul>
<h2>60 vs 90분</h2>
<p>처음·바쁜 직장인 <strong>60분</strong>, 전신 이완 원하면 <strong>90분</strong>. 금액권 7~10만 원이면 60분 1~2회 분량.</p>
<p><a href="../posts/gift-card-basics-guide.html">기프트카드 입문</a>과 함께 보세요.</p>
<h2>첫 방문 안내 메모</h2>
<ol>
<li>샤워·라커 이용 가능 여부</li>
<li>예약 10분 전 도착</li>
<li>통증 있으면 즉시 말하기</li>
</ol>""",
    },
    {
        "id": "luxury-spa-gift-card-guide",
        "title": "프리미엄·호텔 스파 기프트카드 — 럭스 선물의 금액·코스·에티켓",
        "summary": "20만 원대도 아깝지 않은 호텔 스파 기프트. 기념일·거래처·부모님 프리미엄 마사지 기프트카드 가이드.",
        "category": "럭스·프리미엄",
        "tags": ["프리미엄", "호텔스파", "럭스선물"],
        "emoji": "✨",
        "media": "luxe",
        "content": """<p>가끔은 <strong>호텔 스파 120분</strong> 같은 경험을 선물하고 싶을 때가 있습니다. 프리미엄 기프트카드는 금액대가 높아 <strong>유효기간·환불·예약 대기</strong>를 꼼꼼히 봐야 해요.</p>
<h2>금액 가이드</h2>
<ul>
<li>호텔 스파 90분 — 15~25만 원대</li>
<li>커플 패키지 — 30~40만 원</li>
<li>프리미엄 체인 금액권 — 20만 원 충전 후 분할 이용</li>
</ul>
<h2>예약 현실</h2>
<p>인기 호텔은 <strong>2~4주 전</strong> 예약. 기프트카드와 함께 \"원하는 달 미리 전화해 봐\"라고 안내하세요.</p>
<p><a href="../posts/spa-vs-massage-gift.html">스파 vs 동네 마사지</a> 선택 기준.</p>
<div class="article-highlight"><p>럭스 선물은 <strong>경험</strong>을 파는 것—메시지 카드에 \"오늘만큼은 아무것도 하지 마\" 한 줄이면 충분합니다.</p></div>""",
    },
    {
        "id": "seoul-capital-gift-card-tips",
        "title": "서울·수도권 마사지 기프트카드 — 출·퇴근족 선물 지역 가이드",
        "summary": "강남·홍대·분당·일산, 수도권 직장인에게 통하는 마사지 기프트카드. 전국 이용 vs 지역 한정 선택법.",
        "category": "서울·수도권",
        "tags": ["서울", "수도권", "마사지기프트"],
        "emoji": "🏙️",
        "media": "gift",
        "content": """<p>수도권은 <strong>지점 수</strong>가 많아 기프트카드 선택지가 넓습니다. 반대로 \"어디서 쓰지?\" 막막할 수 있어, <strong>전국 이용 가능 브랜드</strong> vs <strong>단골 샵 지정</strong> 중 하나를 골라 주는 게 좋아요.</p>
<h2>직장인 패턴별 추천</h2>
<ul>
<li><strong>강남·역삼</strong> — 야근 후 21시 이후 영업 샵 확인</li>
<li><strong>홍대·마포</strong> — 주말 예약 경쟁, 미리 잡기</li>
<li><strong>분당·판교</strong> — IT·금융, 점심·저녁 슬롯</li>
</ul>
<h2>교통·주차</h2>
<p>기프트카드 메모에 \"○○역 3번 출구 5분\" 샵 이름을 적어 주면 이용률이 올라갑니다.</p>
<p>샵 비교는 <a href="https://gunmacity.com/" target="_blank" rel="noopener noreferrer">마사지</a> 정보 검색 후, 기프트카드 가맹 여부를 확인하세요.</p>""",
    },
    {
        "id": "regional-national-gift-card",
        "title": "부산·대구·광주 — 지방 거주 지인에게 마사지 기프트카드 보내기",
        "summary": "수도권 브랜드가 지방에서도 되나? 전국 체인·지역 샵 기프트카드 선물 시 확인할 것.",
        "category": "지방·전국",
        "tags": ["지방", "전국이용", "마사지기프트"],
        "emoji": "🗺️",
        "media": "warm",
        "content": """<p>서울에 사는 분이 부산·대구 친구에게 기프트카드를 보낼 때 가장 많이 하는 실수는 <strong>수도권 전용 카드</strong>를 사는 것입니다. 구매 전 \"전국 매장\" 또는 \"온라인 예약 가능 지역\"을 반드시 확인하세요.</p>
<h2>전국 vs 지역</h2>
<table class="article-table">
<tr><th>유형</th><th>장점</th><th>주의</th></tr>
<tr><td>전국 체인 금액권</td><td>이사·출장 후에도 사용</td><td>지점 없는 도시 확인</td></tr>
<tr><td>지역 샵 지정</td><td>동네 단골 퀄리티</td><td>타 지역 이용 불가</td></tr>
</table>
<h2>디지털이 유리한 이유</h2>
<p>택배 없이 당일 전달, 친구가 <strong>자기 동네 샵</strong>에 맞는 카드로 교환 가능한지도 체크.</p>
<p><a href="../posts/digital-gift-card-tips.html">디지털 가이드</a> 참고.</p>""",
    },
    {
        "id": "senior-70s-massage-gift",
        "title": "70대 부모님·어르신 마사지 기프트카드 — 안전하고 부드러운 코스 고르기",
        "summary": "고령층 맞춤 저압·짧은 시간·동행 팁. 어르신께 드리는 마사지 기프트카드 실전 가이드.",
        "category": "시니어·어르신",
        "tags": ["어르신", "시니어", "효도선물"],
        "emoji": "🌸",
        "media": "warm",
        "content": """<p>70대 이상 어르신께 마사지 기프트카드는 <strong>허리·무릎·어깨</strong> 불편을 완화하는 데 도움이 될 수 있지만, 강한 압·긴 시간은 부담일 수 있어요. \"부드럽게, 50~60분\"을 예약·현장 모두에서 요청하세요.</p>
<h2>안전 체크</h2>
<ul>
<li>골다공증·혈전·개방성 상처 — 이용 전 상담</li>
<li>혈압·당뇨약 — 샵에 알리기</li>
<li>미끄러운 복도·계단 — 매장 환경 문의</li>
</ul>
<h2>동행 선물</h2>
<p>카드 + \"다음 주말에 같이 가요\"가 최고의 패키지. <a href="../posts/gift-for-parents-massage.html">부모님 선물</a> 글과 연결해 보세요.</p>
<h2>금액</h2>
<p>5~7만 원, 60분 스웨디시·아로마(저압). 90분은 피로 누적 시에만.</p>""",
    },
    {
        "id": "gen-z-gift-card-trend-2026",
        "title": "2030 세대 마사지 기프트카드 트렌드 — 2026 MZ 선물 소비 리포트",
        "summary": "카톡·인스타 DM으로 보내는 e-기프트, 3만 원대 소액·경험 선물. MZ가 좋아하는 마사지 기프트카드 패턴.",
        "category": "2030·트렌드",
        "tags": ["MZ", "2030", "트렌드"],
        "emoji": "📱",
        "media": "calm",
        "content": """<p>2030 세대 선물 소비는 <strong>경험</strong>과 <strong>즉시 전달</strong> 쪽으로 기울어 있습니다. 7월 기준, 마사지 기프트카드도 \"실물 카드\"보다 <strong>카톡 e-쿠폰</strong> 비중이 높아지는 추세예요—물론 취향은 사람마다 다릅니다.</p>
<h2>관찰되는 패턴</h2>
<ul>
<li><strong>3~5만 원</strong> 소액 다회보다 <strong>7만 원 1회</strong> 집중</li>
<li>발렌타인·생일 <strong>당일 0시</strong> 디지털 발송</li>
<li>\"같이 가자\" 커플·친구 <strong>2장 세트</strong></li>
<li>인스타-worthy 호텔 스파 vs 동네 실속샵 <strong>반반</strong></li>
</ul>
<h2>실수 피하기</h2>
<p>너무 큰 금액(부담), 유효기간 짧음, 특정 성별 전용 샵(친구 성별·취향 확인).</p>
<p><a href="../posts/digital-gift-card-tips.html">디지털 발송</a>, <a href="../posts/couple-massage-gift.html">커플 선물</a> 참고.</p>""",
    },
    {
        "id": "friendship-gift-card-guide",
        "title": "친구·절친에게 마사지 기프트카드 — 우정 선물 금액·메시지 아이디어",
        "summary": "생일·이직·고민 들어준 답례. 친구 관계에 맞는 마사지 기프트카드, 부담 없는 금액대.",
        "category": "친구·우정",
        "tags": ["친구선물", "우정", "마사지기프트"],
        "emoji": "🤝",
        "media": "sunset",
        "content": """<p>친구 선물은 <strong>부담 없음</strong>과 <strong>쓸모</strong> 사이에서 밸런스를 맞춰야 합니다. 마사지 기프트카드는 \"술 한잔 값으로 등 한번 풀어\"라는 메시지로 잘 맞아요.</p>
<h2>상황별 금액</h2>
<ul>
<li>생일·1000일 — 5~7만 원</li>
<li>취업·이직 축하 — 7~10만 원</li>
<li>고민 들어준 답례 — 5만 원 + 커피 쿠폰</li>
</ul>
<h2>함께 vs 혼자</h2>
<p>\"너만 가\"보다 \"다음에 같이 가자, 네 것만 내가 쏠게\"가 거절률이 낮습니다. 2장 구매 시 <strong>동일 금액</strong>이 깔끔.</p>
<p><a href="../posts/birthday-wellness-gift.html">생일 웰니스</a> 가이드도 참고하세요.</p>""",
    },
    {
        "id": "overseas-remote-gift-card",
        "title": "해외 거주 가족·친구에게 마사지 기프트카드 — 원격 선물 실전법",
        "summary": "한국에 있는 부모님·연인에게 디지털로 보내는 마사지 기프트카드. 해외에서 결제·발송하는 방법.",
        "category": "해외·원격",
        "tags": ["해외", "원격선물", "디지털"],
        "emoji": "✈️",
        "media": "calm",
        "content": """<p>해외에 있어도 <strong>한국 내 이용 가능</strong> 마사지 기프트카드는 디지털로 보낼 수 있습니다. 부모님 생신·명절에 \"옆에 없어도 마음은 전한다\"는 선택지예요.</p>
<h2>구매·발송 경로</h2>
<ul>
<li>국내 브랜드 공식 앱·웹 (해외 카드 결제 가능 여부 확인)</li>
<li>국내 지인에게 금액 송금 후 대신 구매</li>
<li>전국 체인 e-기프트 (카카오·문자)</li>
</ul>
<h2>받는 분 안내</h2>
<ol>
<li>유효기간·잔액 확인법(앱·전화)</li>
<li>한국 전화번호로 예약</li>
<li>가까운 지점 리스트 (구글맵 검색)</li>
</ol>
<p><a href="../posts/digital-gift-card-tips.html">디지털 발송</a>, <a href="../posts/how-to-use-massage-gift.html">사용법</a> 필독.</p>""",
    },
    {
        "id": "team-building-gift-card-bulk",
        "title": "팀·부서 단체 마사지 기프트카드 — 프로젝트 종료·워크숍 선물",
        "summary": "5~20명 단위 기업·스타트업 팀 선물. 단체 구매·금액 통일·세금계산서·복지 포인트 활용.",
        "category": "단체·팀",
        "tags": ["단체", "팀", "기업선물"],
        "emoji": "👥",
        "media": "gift",
        "content": """<p>프로젝트 끝·분기 마감 후 팀에 <strong>마사지 기프트카드</strong>를 돌리면 회식보다 부담이 적다는 피드백이 많습니다. 7월 하반기 결산 전, \"고생했어\" 한마디와 함께 쓰기 좋아요.</p>
<h2>단체 구매 팁</h2>
<ul>
<li><strong>동일 금액</strong> 5~7만 원 통일 (서열 이슈 완화)</li>
<li>브랜드 <strong>전국 이용</strong> (재택·지방 인원 포함)</li>
<li>대량 구매 할인·세금계산서 — 담당자에게 문의</li>
</ul>
<p><a href="../posts/corporate-gift-card.html">직장·거래처 선물</a>와 함께 보세요.</p>
<h2>전달 방식</h2>
<p>개별 디지털 발송 또는 팀 채팅 + \"이번 주 안에 꼭 쓰기\" 유머 한 스푼.</p>""",
    },
    {
        "id": "wfh-neck-shoulder-gift",
        "title": "재택·장시간 PC 마사지 기프트카드 — 목·어깨 집중 선물",
        "summary": "WFH·IT·디자이너에게. 거북목·어깨 결림 타깃 60분 코스 기프트카드 선택법.",
        "category": "재택·WFH",
        "tags": ["재택", "WFH", "목어깨"],
        "emoji": "💻",
        "media": "nature",
        "content": """<p>재택근무가 늘면서 <strong>목·어깨·손목</strong> 불편을 호소하는 지인이 많아졌습니다. \"거북목 스트레칭 영상 보내기\" 다음 단계가 <strong>60분 상체 마사지 기프트카드</strong>예요.</p>
<h2>코스 키워드</h2>
<p>예약 시 \"데스크워크·상체 집중·목어깨\"라고 말하면 샵에서 이해합니다. 전신 90분보다 <strong>60분 집중</strong>이 현실적.</p>
<h2>타이밍</h2>
<ul>
<li>분기 마감 직후</li>
<li>대규모 업데이트·런칭 후</li>
<li>연차 쓰기 직전 \"회복용\"</li>
</ul>
<p><a href="../posts/nail-art-hand-massage-gift.html">손·팔 마사지</a> 글도 타이핑 많은 분께 참고.</p>""",
    },
    {
        "id": "rainy-season-massage-gift",
        "title": "장마철 마사지 기프트카드 — 습기·뻐근함, 7월 선물 아이디어",
        "summary": "비 오는 날 집콕 대신 실내 힐링. 장마·습도 시즌에 어울리는 마사지 기프트카드와 이용 팁.",
        "category": "장마·습기",
        "tags": ["장마", "7월", "힐링"],
        "emoji": "🌧️",
        "media": "calm",
        "content": """<p>7월 <strong>장마</strong>—습도가 높으면 몸이 무겁고 관절이 뻐근하게 느껴지는 분들이 많습니다. 실내에서 온기 있는 마사지는 \"비 오는 날 할 일\"로 제격이에요.</p>
<h2>장마철 마사지 팁</h2>
<ul>
<li>마사지 후 <strong>강한 냉방</strong>·창문 옆 자리 피하기</li>
<li>습한 날 <strong>발·종아리</strong> 부종 — 림프·하체 코스</li>
<li>우산·옷 젖음 — 샵에 도착 시간 여유</li>
</ul>
<h2>선물 메시지</h2>
<p>\"장마에 우울할 때, 따뜻한 방에서 1시간만 쉬어.\"</p>
<p>여름 휴가 선물과 비교는 <a href="../blog/summer-vacation-massage-gift-2026.html">여름 휴가철 가이드</a> 참고.</p>""",
    },
    {
        "id": "gift-card-expiry-rights-guide",
        "title": "마사지 기프트카드 유효기간·소멸시효 — 2026 소비자 권리 정리",
        "summary": "1년·3년·5년, 연장·환불·잔액. 기프트카드 유효기간과 법적 권리, 선물 전 확인할 약관.",
        "category": "유효기간·권리",
        "tags": ["유효기간", "소비자", "환불"],
        "emoji": "📋",
        "media": "gift",
        "content": """<p>기프트카드를 선물할 때 <strong>유효기간</strong>은 받는 분의 \"쓸 수 있는 시간\"입니다. 7월에 산 카드가 내년 6월까지인지, 2028년까지인지—<strong>구매 전 화면 캡처</strong>를 공유하는 것도 배려예요.</p>
<h2>확인 항목</h2>
<ol>
<li>유효기간 시작일(구매일 vs 최초 사용일)</li>
<li>연장 1회 가능 여부·비용</li>
<li>미사용 잔액 60% 이상 환불 규정(전자상거래 등)</li>
<li>양도·재판매 금지 조항</li>
</ol>
<h2>선물자가 적어 줄 메모</h2>
<p>\"유효기간 ○○까지, 앱에서 ○○ 메뉴 → 잔액 조회\"</p>
<p><a href="../posts/how-to-use-massage-gift.html">사용법</a>, <a href="../posts/gift-card-basics-guide.html">입문 가이드</a> 연계.</p>
<div class="warn-box"><strong>주의</strong> 개별 약관은 브랜드마다 다릅니다. 구매 페이지 최종 확인 필수.</div>""",
    },
    {
        "id": "first-visit-booking-guide-gift",
        "title": "마사지 기프트카드 첫 사용 — 예약·샤워·팁까지 완전 정리",
        "summary": "카드 받고 막막한 분을 위한 A to Z. 첫 방문 예약, 샤워·시간·매너, 기프트카드 결제 흐름.",
        "category": "첫방문·예약",
        "tags": ["첫방문", "예약", "이용법"],
        "emoji": "📅",
        "media": "luxe",
        "content": """<p>마사지 기프트카드를 <strong>처음</strong> 받으면 \"지금 전화해야 하나?\"부터 막막합니다. 7월, 미리 알아두면 유효기간 안에 여유 있게 쓸 수 있어요.</p>
<h2>예약 순서</h2>
<ol>
<li>카드 뒷면·문자의 <strong>예약 번호</strong> 확인</li>
<li>전화·앱·카톡 중 안내된 채널 선택</li>
<li>코스·시간·성별 테라피스트 요청(가능 시)</li>
<li>기프트카드 번호·PIN 예약 시 등록</li>
</ol>
<h2>당일</h2>
<ul>
<li>10분 전 도착, 샤워 가능 여부 확인</li>
<li>압력·아픈 부위 미리 말하기</li>
<li>팁(사후)은 필수 아님—문화·샵마다 다름</li>
</ul>
<p>상세는 <a href="../posts/how-to-use-massage-gift.html">기프트카드 사용법</a> 글을 참고하세요.</p>
<p>샵 찾기: <a href="https://gunmacity.com/" target="_blank" rel="noopener noreferrer">마사지</a> 검색 후 전화로 기프트카드 가능 여부 문의.</p>""",
    },
]


def main() -> None:
    for p in NEW_POSTS:
        p.setdefault("author", "기프트카드")
        p.setdefault("date", DATE)
        p.setdefault("published", True)

    existing = json.loads(POSTS_PATH.read_text(encoding="utf-8"))
    by_id = {x["id"]: x for x in existing.get("posts", [])}
    for p in NEW_POSTS:
        by_id[p["id"]] = p
    merged = list(by_id.values())
    merged.sort(key=lambda x: x.get("date", ""), reverse=True)
    POSTS_PATH.write_text(
        json.dumps({"posts": merged}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Added/updated {len(NEW_POSTS)} posts. Total: {len(merged)}")


if __name__ == "__main__":
    main()
