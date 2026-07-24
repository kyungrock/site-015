#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-07-23 블로그 20편 — 카테고리 중복 없음 · SEO · 적당히 긴 본문"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POSTS_PATH = ROOT / "data" / "blog-posts.json"
DATE = "2026-07-23"

NEW_POSTS = [
    {
        "id": "birthday-massage-gift-card-2026",
        "title": "생일 선물로 마사지 기프트카드 — 케이크 대신 고르는 현실적인 힐링 선물",
        "summary": "생일 마사지 기프트카드 금액·코스·메시지 템플릿. 친구·연인·동료 생일까지 SEO에 맞춘 선택 가이드.",
        "category": "생일·기념일",
        "tags": ["생일선물", "마사지기프트카드", "기념일선물"],
        "emoji": "🎂",
        "media": "gift",
        "content": """
<p>케이크와 꽃다발은 예쁘지만, 다음 날이면 남기지 않습니다. <strong>생일 마사지 기프트카드</strong>는 “오늘 하루 네 몸을 쉬게 해”라는 메시지를 길게 남깁니다. 2026년 기준으로 실패 없는 고르는 법을 정리했습니다.</p>
<h2>관계별 적정 금액</h2>
<table class="article-table">
<tr><th>관계</th><th>금액</th><th>추천 코스</th></tr>
<tr><td>친구·동료</td><td>3~5만</td><td>부분·풋 45분</td></tr>
<tr><td>연인·가족</td><td>7~12만</td><td>스웨디시 60~90분</td></tr>
<tr><td>특별한 해</td><td>15만+</td><td>스파·아로마 콤보</td></tr>
</table>
<p>금액 분포는 <a href="../posts/gift-card-amount-guide.html">금액 가이드</a>, 생일 웰니스는 <a href="../posts/birthday-wellness-gift.html">생일 웰니스 선물</a>도 참고하세요.</p>
<h2>메시지 한 줄</h2>
<p>“케이크 대신 어깨 풀 시간 보냈어요. 편한 날 예약하세요.” — 짧을수록 부담이 적습니다.</p>
<h2>SEO로 챙길 키워드</h2>
<p>‘생일 마사지 선물’, ‘생일 기프트카드 추천’, ‘직장인 생일 힐링’처럼 구체적 검색어를 제목·요약·본문에 자연스럽게 넣으면 발견성이 좋아집니다.</p>
<p>근처 매장: <a href="https://gunmacity.com/" target="_blank" rel="noopener noreferrer">마사지</a></p>
""",
    },
    {
        "id": "autumn-transition-massage-gift-2026",
        "title": "환절기·초가을 마사지 기프트카드 — 에어컨 피로에서 벗어나는 7~9월 선물",
        "summary": "환절기 목·어깨·면역 저하 시즌에 맞는 마사지 기프트카드. 초가을 전 미리 준비하는 실전 팁.",
        "category": "환절기·가을",
        "tags": ["환절기", "가을선물", "마사지기프트"],
        "emoji": "🍂",
        "media": "nature",
        "content": """
<p>7월 말~9월은 냉방과 야외 열기가 교차하는 <strong>환절기</strong>입니다. 어깨가 굳고 목이 뻐근해질 때 <strong>마사지 기프트카드</strong>는 시즌 선물로 잘 맞습니다.</p>
<h2>환절기에 잘 맞는 코스</h2>
<ul>
<li>목·어깨 집중 45~60분</li>
<li>저~중압 스웨디시 (강압은 컨디션 보고)</li>
<li>온열·핫스톤은 개인 체온에 맞게</li>
</ul>
<h2>선물 타이밍</h2>
<p>장마가 끝난 직후, 추석 준비 전—검색량도 ‘환절기 마사지’, ‘가을 힐링 선물’로 움직입니다. 미리 사 두면 받는 사람이 여유 있게 예약할 수 있습니다.</p>
<p>장마철 글과 겹치지 않게, 이번엔 <strong>일교차·냉방병</strong>에 초점을 둡니다. 사용법: <a href="../posts/how-to-use-massage-gift.html">기프트카드 사용법</a></p>
<div class="tip-box"><strong>팁</strong> 감기 기운이 있을 때는 방문 연기를 메시지에 한 줄 적어 주세요.</div>
""",
    },
    {
        "id": "neck-shoulder-focus-gift-card",
        "title": "목·어깨 집중 마사지 기프트카드 — 거북목·모니터병에 맞춘 부분 관리 선물",
        "summary": "전신보다 목·어깨만 풀어 주는 부분 마사지 기프트카드. 직장인·학생에게 통하는 금액과 예약 팁.",
        "category": "목어깨·집중",
        "tags": ["목어깨마사지", "거북목", "부분관리", "기프트카드"],
        "emoji": "💆",
        "media": "warm",
        "content": """
<p>전신 90분이 부담스럽다면 <strong>목·어깨 집중 마사지 기프트카드</strong>가 정답인 경우가 많습니다. 모니터·스마트폰으로 굳은 승모근만 풀어 줘도 “필요했다”는 반응이 나옵니다.</p>
<h2>부분 관리가 선물로 좋은 이유</h2>
<ul>
<li>30~60분이라 점심·퇴근 후에도 가능</li>
<li>탈의·샤워 부담이 상대적으로 적음</li>
<li>3~7만 원대에서 가성비가 좋음</li>
</ul>
<p>재택·장시간 PC 글과 달리, 여기는 <strong>코스 명칭·압력·예약 슬롯</strong>에 집중합니다. 관련: <a href="../blog/wfh-neck-shoulder-gift.html">재택 목·어깨 글</a></p>
<h2>예약 시 말할 문구</h2>
<p>“기프트카드로 목·어깨 부분 관리 예약하고 싶어요. 압력은 중압으로요.”</p>
<p>매장 검색: <a href="https://gunmacity.com/" target="_blank" rel="noopener noreferrer">마사지</a></p>
""",
    },
    {
        "id": "deep-tissue-massage-gift-guide",
        "title": "딥티슈·강압 마사지 기프트카드 — 받을 사람 성향 먼저 보고 고르는 법",
        "summary": "딥티슈 마사지 선물은 취향이 갈립니다. 강압을 좋아하는 분께만 주는 기프트카드 선택·주의사항.",
        "category": "딥티슈·강압",
        "tags": ["딥티슈", "강압마사지", "마사지기프트카드"],
        "emoji": "💪",
        "media": "gift",
        "content": """
<p><strong>딥티슈 마사지 기프트카드</strong>는 “제대로 풀리고 싶다”는 분께는 최고지만, 이완만 원하는 분께는 부담이 됩니다. 선물 전에 취향을 한 번만 확인하세요.</p>
<h2>딥티슈가 맞는 사람</h2>
<ul>
<li>운동·헬스 후 근육통이 잦은 분</li>
<li>스웨디시가 “너무 약하다”고 했던 분</li>
<li>만성 어깨·등 뭉침을 세게 푸는 편을 선호</li>
</ul>
<h2>피해야 할 경우</h2>
<p>고령·임산부·혈압·최근 부상·마사지 입문자에게는 스웨디시·부분 이완이 안전합니다. 입문용은 <a href="../blog/swedish-massage-gift-intro.html">스웨디시 입문</a>을 권합니다.</p>
<h2>메시지 예시</h2>
<p>“세게 푸는 거 좋아한다고 해서 딥티슈 가능한 금액권으로 골랐어요. 당일 압력 조절 말씀하세요.”</p>
""",
    },
    {
        "id": "hot-stone-massage-gift-2026",
        "title": "핫스톤·온열 마사지 기프트카드 — 여름밤 에어컨 한기 풀리는 선물",
        "summary": "핫스톤 마사지 기프트카드의 장점, 여름·환절기 활용법, 화상·금기 체크리스트.",
        "category": "핫스톤·온열",
        "tags": ["핫스톤", "온열마사지", "기프트카드"],
        "emoji": "🔥",
        "media": "warm",
        "content": """
<p>에어컨 바람에 등이 서늘해진 날, <strong>핫스톤·온열 마사지 기프트카드</strong>는 체감 만족도가 높습니다. 돌의 온기로 근육을 느슨하게 풀어 주는 코스입니다.</p>
<h2>이런 분께 추천</h2>
<ul>
<li>냉방·한기로 등이 굳는 분</li>
<li>이완·수면 전 케어를 원하는 분</li>
<li>특별한 날 스파 느낌을 주고 싶을 때</li>
</ul>
<h2>주의</h2>
<p>피부 민감·당뇨·임산부·고열 시에는 샵에 먼저 문의. 온도를 낮춰 달라고 요청할 수 있다고 메시지에 적어 주세요.</p>
<p>스파 vs 마사지: <a href="../posts/spa-vs-massage-gift.html">스파와 마사지 비교</a></p>
""",
    },
    {
        "id": "head-spa-scalp-gift-card",
        "title": "헤드스파·두피 마사지 기프트카드 — 두통·눈 피로에 가벼운 힐링 선물",
        "summary": "헤드스파·두피 케어 기프트카드 고르는 법. 짧은 시간·적은 부담으로 고마움을 전하는 SEO 가이드.",
        "category": "헤드스파·두피",
        "tags": ["헤드스파", "두피마사지", "기프트카드"],
        "emoji": "🧴",
        "media": "nature",
        "content": """
<p>전신이 부담스러울 때 <strong>헤드스파·두피 마사지 기프트카드</strong>는 가볍고 세련된 선택입니다. 눈 피로·긴장성 두통·수면 전 루틴에 잘 맞습니다.</p>
<h2>장점</h2>
<ul>
<li>30~60분으로 짧게 끝남</li>
<li>헤어·메이크업 후 일정도 조율 가능(샵마다 다름)</li>
<li>금액대가 비교적 낮아 거절이 적음</li>
</ul>
<h2>전달 멘트</h2>
<p>“요즘 모니터 많이 본다 해서 머리·두피 풀 수 있는 걸로 보냈어요.”</p>
<p>첫 방문: <a href="../blog/first-visit-booking-guide-gift.html">첫 사용 가이드</a> · 매장: <a href="https://gunmacity.com/" target="_blank" rel="noopener noreferrer">마사지</a></p>
""",
    },
    {
        "id": "mens-healing-massage-gift",
        "title": "남성·신사 마사지 기프트카드 — 취향 안 맞춰도 실패 적은 실용 선물",
        "summary": "남성에게 주는 마사지 기프트카드. 스포츠·스웨디시·금액대와 ‘부담 없는’ 메시지 작성법.",
        "category": "남성·힐링",
        "tags": ["남성선물", "신사선물", "마사지기프트카드"],
        "emoji": "🧔",
        "media": "gift",
        "content": """
<p>향수·넥타이는 취향이 갈리지만, <strong>남성 마사지 기프트카드</strong>는 “몸만 풀면 된다”는 실용성으로 통과하기 쉽습니다. 아버지·남편·남동생·남성 동료에게 통합니다.</p>
<h2>코스 추천</h2>
<ul>
<li>헬스·구기 운동 → 스포츠·딥티슈 가능권</li>
<li>사무직 → 목·어깨·스웨디시</li>
<li>첫 경험 → 60분 중압 이하</li>
</ul>
<p>스포츠 회복: <a href="../blog/sports-recovery-gift-card.html">스포츠 기프트 가이드</a></p>
<h2>메시지</h2>
<p>“뭘 사 드릴지 몰라서, 편한 날 몸 풀라고 금액권으로 준비했어요.”</p>
""",
    },
    {
        "id": "womens-beauty-massage-gift",
        "title": "여성·뷰티 마사지 기프트카드 — 에스테·이완을 섞어 고르는 센스",
        "summary": "여성 선물로 마사지·바디·아로마 기프트카드를 고를 때 코스·향·금액 체크리스트.",
        "category": "여성·뷰티",
        "tags": ["여성선물", "뷰티기프트", "바디마사지"],
        "emoji": "✨",
        "media": "warm",
        "content": """
<p><strong>여성·뷰티 마사지 기프트카드</strong>는 단순 이완뿐 아니라 스크럽·아로마·바디 케어가 붙은 코스가 인기입니다. 다만 향·오일 알레르기는 미리 짚어 주세요.</p>
<h2>고를 때 체크</h2>
<ol>
<li>무향·저자극 옵션 가능 여부</li>
<li>스크럽+마사지 콤보인지</li>
<li>네일·헤어 일정과 충돌하지 않는지</li>
</ol>
<p>아로마: <a href="../blog/aroma-gift-card-scent-guide.html">향기 가이드</a> · 핸드·네일 연계: <a href="../posts/nail-art-hand-massage-gift.html">네일·핸드 마사지</a></p>
<div class="tip-box"><strong>팁</strong> “향 민감하시면 무향으로요”를 카드 메시지에 넣으면 섬세해 보입니다.</div>
""",
    },
    {
        "id": "exam-student-massage-gift-2026",
        "title": "수험생·입시생 부모 선물 — 시험 후 회복용 마사지 기프트카드",
        "summary": "수능·내신·자격증 시험 전후, 수험생·학부모에게 주는 마사지 기프트카드 에티켓과 코스.",
        "category": "수험·입시",
        "tags": ["수험생선물", "입시", "마사지기프트"],
        "emoji": "📚",
        "media": "nature",
        "content": """
<p>시험 직전에는 자극을 줄이고, <strong>시험이 끝난 뒤</strong>에 쓰는 <strong>수험·입시 마사지 기프트카드</strong>가 안전합니다. 목·어깨·두피 이완이 현실적인 선택입니다.</p>
<h2>타이밍</h2>
<ul>
<li>시험 전: 가벼운 풋·헤드만, 강압 금지</li>
<li>시험 후: 스웨디시·부분 60분</li>
<li>학부모 본인에게: “당신도 쉬라”는 메시지</li>
</ul>
<h2>에티켓</h2>
<p>성적·합불을 언급하지 말고, “고생했다 / 어깨 풀자”에만 집중하세요.</p>
<p>사용법: <a href="../posts/how-to-use-massage-gift.html">기프트카드 사용법</a></p>
""",
    },
    {
        "id": "discharge-military-massage-gift",
        "title": "군인·제대 선물로 마사지 기프트카드 — 훈련·경계 뒤 몸을 위한 현실 선물",
        "summary": "입대·면회·제대 선물로 마사지 기프트카드를 고를 때의 금액, 전국 사용처, 전달 방법.",
        "category": "군인·제대",
        "tags": ["제대선물", "군인선물", "마사지기프트카드"],
        "emoji": "🎖️",
        "media": "gift",
        "content": """
<p>과자·용돈 다음으로 실용적인 것이 <strong>군인·제대 마사지 기프트카드</strong>입니다. 전역 후 첫 휴가·일상 복귀 때 “몸부터 풀자”는 메시지가 됩니다.</p>
<h2>포인트</h2>
<ul>
<li>전국·지방 사용 가능권 우선</li>
<li>유효기간 12개월 이상 (일정 불확실)</li>
<li>디지털 전달이 면회·택배보다 쉬움</li>
</ul>
<p>지방 사용: <a href="../blog/regional-national-gift-card.html">지방·전국 가이드</a> · 모바일: <a href="../blog/kakao-mobile-massage-gift-send.html">카톡 보내기</a></p>
""",
    },
    {
        "id": "caregiver-hospital-massage-gift",
        "title": "간병·보호자 힐링 선물 — 병간호 지친 가족에게 마사지 기프트카드",
        "summary": "간병·보호자에게 주는 마사지 기프트카드. 짧은 코스, 병원 근처 매장, 따뜻한 메시지 가이드.",
        "category": "간병·보호자",
        "tags": ["간병선물", "보호자", "힐링기프트"],
        "emoji": "🤝",
        "media": "warm",
        "content": """
<p>환자 선물은 많아도, <strong>간병하는 사람</strong>을 챙기는 선물은 드뭅니다. <strong>보호자용 마사지 기프트카드</strong>는 “당신도 쉬어야 한다”는 허락입니다.</p>
<h2>현실적인 조건</h2>
<ul>
<li>병원·집 근처 20분 이내 매장</li>
<li>45~60분 짧은 코스</li>
<li>당일·평일 낮 예약 가능 여부</li>
</ul>
<p>야근·교대 글과 결이 비슷하지만, 여기는 <strong>병간호 피로</strong>에 초점을 둡니다.</p>
<p>메시지: “환자분도 중요하지만, 보호자님 어깨도 좀 풀으세요.”</p>
<p>매장: <a href="https://gunmacity.com/" target="_blank" rel="noopener noreferrer">마사지</a></p>
""",
    },
    {
        "id": "post-travel-massage-gift-2026",
        "title": "여행·출장 후 회복 마사지 기프트카드 — 비행·KTX 피로를 푸는 선물",
        "summary": "해외여행·국내 출장 뒤 붓기·시차로 지친 분께 주는 마사지 기프트카드 코스와 타이밍.",
        "category": "여행·출장후",
        "tags": ["여행후마사지", "출장회복", "기프트카드"],
        "emoji": "✈️",
        "media": "nature",
        "content": """
<p>캐리어를 풀자마자 필요한 것은 또 다른 일정이 아니라 휴식입니다. <strong>여행·출장 후 마사지 기프트카드</strong>는 귀국·귀경 다음날 쓰라고 주면 효과가 큽니다.</p>
<h2>추천 코스</h2>
<ul>
<li>풋·종아리 — 기내·버스 부종</li>
<li>목·어깨 — 노트북 출장</li>
<li>전신 이완 — 장기 여행 후</li>
</ul>
<p>해외 거주 전달과 구분: 이번 글은 <strong>여행 직후 회복</strong>입니다. 해외 원격은 <a href="../blog/overseas-remote-gift-card.html">해외·원격</a>을 보세요.</p>
""",
    },
    {
        "id": "brand-compare-massage-gift-card",
        "title": "마사지 기프트카드 브랜드·유형 비교 — 금액권·횟수권·특정샵권 차이",
        "summary": "마사지 기프트카드 사기 전 비교표. 금액권 vs 횟수권 vs 특정 매장권, SEO 검색자가 묻는 핵심 차이.",
        "category": "브랜드·비교",
        "tags": ["기프트카드비교", "금액권", "마사지기프트"],
        "emoji": "⚖️",
        "media": "gift",
        "content": """
<p>“어떤 마사지 기프트카드가 좋아요?”의 답은 브랜드 이름보다 <strong>유형</strong>에 있습니다. 금액권·횟수권·특정샵권을 비교해 보세요.</p>
<h2>한눈에 보는 차이</h2>
<table class="article-table">
<tr><th>유형</th><th>장점</th><th>단점</th></tr>
<tr><td>금액권</td><td>코스 자유</td><td>추가금 발생 가능</td></tr>
<tr><td>횟수권</td><td>코스 고정·명확</td><td>업그레이드 제한</td></tr>
<tr><td>특정샵권</td><td>퀄리티 예측</td><td>거리·일정 제약</td></tr>
</table>
<p>쿠폰과의 차이: <a href="../posts/gift-card-vs-coupon.html">기프트카드 vs 쿠폰</a> · 기초: <a href="../posts/gift-card-basics-guide.html">기초 가이드</a></p>
""",
    },
    {
        "id": "yearend-massage-gift-prep-2026",
        "title": "연말·송년 마사지 기프트카드 — 11~12월 전에 미리 준비하는 선물 리스트",
        "summary": "연말 거래처·팀·가족 선물로 마사지 기프트카드를 여름·가을에 미리 준비하는 이유와 금액대.",
        "category": "연말·송년",
        "tags": ["연말선물", "송년회", "마사지기프트카드"],
        "emoji": "🎄",
        "media": "gift",
        "content": """
<p>11월이 되면 웰니스 기프트가 품절·배송 지연이 잦습니다. <strong>연말·송년 마사지 기프트카드</strong>는 7~9월에 후보를 정해 두면 여유가 생깁니다.</p>
<h2>대상별 예산</h2>
<ul>
<li>팀원 개인 — 3~5만 소액권</li>
<li>주요 거래처 — 내부 규정 내 VIP권</li>
<li>가족 — 7~15만 프리미엄</li>
</ul>
<p>VIP 답례: <a href="../blog/vip-client-thankyou-massage-gift.html">VIP·고객답례</a> · 홀리데이: <a href="../posts/holiday-season-gift.html">시즌 선물</a></p>
""",
    },
    {
        "id": "business-trip-gift-card-etiquette",
        "title": "비즈니스·출장 동행 선물 — 미팅 상대·同行에게 주는 마사지 기프트카드 에티켓",
        "summary": "비즈니스 출장·미팅 후 답례로 마사지 기프트카드를 줄 때 금액·톤·컴플라이언스 주의점.",
        "category": "비즈니스·출장",
        "tags": ["출장선물", "비즈니스선물", "마사지기프트"],
        "emoji": "🧳",
        "media": "gift",
        "content": """
<p>식사 접대 대신 <strong>비즈니스용 마사지 기프트카드</strong>를 택하는 회사가 늘고 있습니다. 다만 공직·대기업은 상한·신고 규정을 먼저 확인하세요.</p>
<h2>에티켓</h2>
<ol>
<li>과도한 금액·호텔 초고가권 지양</li>
<li>개인 휴대폰으로 조용히 전달</li>
<li>영수증·품의 가능한 공식 채널 구매</li>
</ol>
<p>기업 구매: <a href="../posts/corporate-gift-card.html">기업 기프트카드</a></p>
""",
    },
    {
        "id": "lymph-circulation-massage-gift",
        "title": "림프·순환 마사지 기프트카드 — 부종·무거움 완화에 관심 있을 때",
        "summary": "림프 배수·순환 케어 콘셉트의 마사지 기프트카드. 의학적 한계와 선물 시 올바른 표현법.",
        "category": "림프·순환",
        "tags": ["림프마사지", "부종", "순환케어", "기프트카드"],
        "emoji": "💧",
        "media": "nature",
        "content": """
<p>다리가 무겁고 붓는다는 분께 <strong>림프·순환 마사지 기프트카드</strong>를 고려할 수 있습니다. 단, 질병 치료 약속처럼 말하지 않는 것이 중요합니다.</p>
<h2>올바른 표현</h2>
<p>추천: “부은 느낌 풀리는 부드러운 순환 케어로 예약해 보세요.”  
비추천: “병을 고친다 / 반드시 빠진다”류 과장.</p>
<h2>금기 안내</h2>
<p>감염·혈전·암 치료 중·임신은 전문의·샵 상담 필수. 메시지에 “예약 시 건강 상태 말씀하세요”를 넣으세요.</p>
""",
    },
    {
        "id": "driver-sedentary-massage-gift",
        "title": "운전·좌식 직장인 마사지 기프트카드 — 택시·버스·장거리 운전 피로 선물",
        "summary": "장시간 운전·좌석 근무자를 위한 허리·골반·어깨 마사지 기프트카드 가이드.",
        "category": "운전·좌식",
        "tags": ["운전자선물", "좌식근무", "허리마사지", "기프트카드"],
        "emoji": "🚗",
        "media": "warm",
        "content": """
<p>택시·버스·영업·장거리 출퇴근—앉아 있는 시간이 긴 분께는 <strong>운전·좌식용 마사지 기프트카드</strong>가 와닿습니다. 허리·골반·어깨를 중심으로 고르세요.</p>
<h2>추천</h2>
<ul>
<li>허리·골반 집중 또는 전신 중압</li>
<li>풋·종아리 콤보 (페달·정체 피로)</li>
<li>유효기간 넉넉히 (교대·콜 일정)</li>
</ul>
<p>매장: <a href="https://gunmacity.com/" target="_blank" rel="noopener noreferrer">마사지</a> · 사용: <a href="../posts/how-to-use-massage-gift.html">사용법</a></p>
""",
    },
    {
        "id": "massage-gift-safety-contraindications",
        "title": "마사지 기프트카드 안전·금기 가이드 — 주기 전에 확인할 건강 체크리스트",
        "summary": "마사지 기프트카드를 주기 전 임신·혈압·피부·수술 등 금기·주의 사항을 SEO형으로 정리.",
        "category": "안전·금기",
        "tags": ["마사지금기", "안전가이드", "기프트카드주의"],
        "emoji": "🛡️",
        "media": "nature",
        "content": """
<p>좋은 선물도 상대 건강을 모르면 독이 될 수 있습니다. <strong>마사지 기프트카드 안전·금기</strong>를 보내기 전에 한 번만 점검하세요.</p>
<h2>예약 전 알리면 좋은 것</h2>
<ul>
<li>임신·수유</li>
<li>고혈압·당뇨·심장 질환</li>
<li>최근 수술·골절·피부 질환</li>
<li>항응고제 등 약물</li>
</ul>
<h2>선물 메시지에 넣을 한 줄</h2>
<p>“예약하실 때 건강 상태만 샵에 말씀해 주세요. 코스·압력 맞춰 주신대요.”</p>
<p>소비자 권리: <a href="../blog/gift-card-expiry-rights-guide.html">유효기간·권리</a></p>
""",
    },
    {
        "id": "promo-event-massage-gift-tips",
        "title": "프로모션·이벤트 마사지 기프트카드 — 할인·증정권 살 때 숨은 조건 읽는 법",
        "summary": "마사지 기프트카드 세일·이벤트 구매 시 유효기간·사용일·추가금 조건을 읽는 SEO 체크리스트.",
        "category": "프로모·이벤트",
        "tags": ["마사지할인", "이벤트기프트", "프로모션"],
        "emoji": "🏷️",
        "media": "gift",
        "content": """
<p>반값 이벤트에 혹하기 전에 <strong>프로모션 마사지 기프트카드</strong>의 작은 글씨를 읽으세요. 할인만큼 제약이 따라오는 경우가 많습니다.</p>
<h2>꼭 확인할 조건</h2>
<ol>
<li>유효기간이 유독 짧지 않은지</li>
<li>주말·피크타임 사용 불가인지</li>
<li>특정 코스만 가능한지</li>
<li>양도·환불 조항</li>
</ol>
<p>가성비 일반론: <a href="../blog/budget-value-massage-gift-card-2026.html">가성비 가이드</a></p>
<div class="tip-box"><strong>팁</strong> 정가 금액권이 제약 없는 프로모션권보다 실사용 만족도가 높은 경우도 있습니다.</div>
""",
    },
    {
        "id": "real-use-review-tips-massage-gift",
        "title": "마사지 기프트카드 실사용 후기 팁 — 예약부터 다녀온 뒤까지 만족도 올리는 법",
        "summary": "기프트카드를 실제로 쓸 때 만족도를 높이는 예약·압력·팁·재방문 노하우. 후기형 SEO 가이드.",
        "category": "실사용·후기",
        "tags": ["마사후기", "기프트카드사용팁", "실사용"],
        "emoji": "📝",
        "media": "warm",
        "content": """
<p>카드를 받은 뒤가 진짜 시작입니다. <strong>마사지 기프트카드 실사용</strong>에서 만족도를 가르는 건 브랜드보다 예약·커뮤니케이션입니다.</p>
<h2>만족도 올리는 순서</h2>
<ol>
<li>유효기간을 캘린더에 넣기</li>
<li>집·직장 가까운 매장 2곳 후보</li>
<li>전화로 “기프트 결제·원하는 부위·압력” 말하기</li>
<li>당일 10분 전 도착, 아픈 부위 재고지</li>
</ol>
<p>첫 방문 상세: <a href="../blog/first-visit-booking-guide-gift.html">첫 사용 가이드</a> · 디지털 저장: <a href="../blog/kakao-mobile-massage-gift-send.html">모바일 보내기</a></p>
<p>매장 찾기: <a href="https://gunmacity.com/" target="_blank" rel="noopener noreferrer">마사지</a></p>
<h2>다녀온 뒤</h2>
<p>당일 과음·격한 운동은 피하고, 수분 섭취. 잔액이 남으면 다음 부분 관리에 쓰면 됩니다.</p>
""",
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
    merged.sort(key=lambda x: (x.get("date", ""), x.get("id", "")), reverse=True)
    POSTS_PATH.write_text(
        json.dumps({"posts": merged}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Added/updated {len(NEW_POSTS)} posts. Total: {len(merged)}")


if __name__ == "__main__":
    main()
