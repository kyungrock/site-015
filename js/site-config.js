/** Deno Deploy 배포 URL (로컬·다른 호스트는 자동 보정) */
window.SITE_CONFIG = {
  baseUrl: "https://site-015-ka9ctrdq9qrd.kyungrock.deno.net",
  siteName: "기프트카드",
  slug: "site-015",
  defaultDescription:
    "마사지 기프트카드 선물 가이드. 힐링·웰니스·셀프케어를 위한 실용 정보 허브.",
  locale: "ko_KR",
  keywords: "마사지기프트,마사지,힐링,웰니스,셀프케어",
};

function getSiteBase() {
  const cfg = window.SITE_CONFIG?.baseUrl;
  if (cfg && !location.hostname.includes("localhost") && !location.protocol.startsWith("file")) {
    return cfg.replace(/\/$/, "");
  }
  const path = location.pathname.replace(/\/[^/]*$/, "");
  return (location.origin + path).replace(/\/$/, "") || location.origin;
}

function absoluteUrl(relativePath) {
  const base = getSiteBase();
  const path = String(relativePath || "")
    .replace(/^\//, "")
    .replace(/^https?:\/\//, "");
  if (path.startsWith("http")) return path;
  return `${base}/${path}`;
}
