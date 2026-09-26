# Awesome Agent Ops

_English version: [README.md](README.md)_

Список о том, что на самом деле нужно, чтобы **личный ИИ-агент работал в проде**: не трюки с
промптами, а скучный слой — расписания, бюджет контекста, секреты, песочницы, доставка и те
поломки, о которых никто не предупреждает.

Всё здесь написано с агента, который работает без присмотра с середины 2026 года на одном
небольшом сервере: кроны в 03:10, Telegram, медицинские данные, почта и GitHub. Практические
заметки ссылаются на серию из 34 модулей, где каждая тема разобрана целиком:
[Hermes-Agent-Ops](https://github.com/ipanalytics/Hermes-Agent-Ops).

---

## 1. Начните с поломок

- **Задача отработала и промолчала** — крон, который падает тихо, хуже того, который падает
  громко. Доставляемость — это метрика, а не надежда. [Модуль 28](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/28-digest-delivery-health).
- **Задача перестала существовать** — расписания дрейфуют: одноразовый крон не перевзвёлся,
  задание «на день» стоит с марта. Проверять надо расписание, а не выпуск. [Модуль 30](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/30-schedule-audit).
- **Отчёт, который никто не прочитал** — выпуск не в тот топик равен невыпуску. Разводить по
  смыслу, а не по привычке. [Модуль 12](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/12-topic-routing).
- **Контекст, который тихо сжался** — компакция незаметна, пока не вынесет нужную деталь.
  Сначала измерьте её цену. [Модуль 31](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/31-compaction-effect-check).

## 2. Работа по расписанию

- **[Крон для кронов](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/05-cron-of-crons)** —
  одно задание, чья единственная цель — заметить, что другое не запустилось.
- **[Линтер свежих промптов](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/07-fresh-prompt-linter)** —
  промпты гниют быстрее кода: ссылаются на задания, файлы и имена, которых уже нет.
- **[Из LLM-задания в скрипт](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/24-llm-to-script)** —
  лучший крон — это скрипт-сборщик плюс небольшой вызов модели в конце, а не петля агента.
- **[Эвалы и вскрытие](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/20-task-evals-and-autopsy)** —
  когда задание упало, восстановите, что оно видело, вместо повторного прогона наугад.

## 3. Контекст и деньги

- **[Управление расходами](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/19-cost-governance)** —
  жёсткий бюджет с мягкой деградацией лучше неожиданного счёта.
- **[Дашборд расходов](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/10-cost-dashboard)** —
  траты по заданиям и моделям, чтобы «агент подорожал» стало числом с причиной.
- **[Слой размышления](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/29-thinking-layer-cost)** —
  платите за рассуждение там, где решение, а не там, где текст.

## 4. Изоляция и секреты

- **[Ограничители инструментов](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/15-agent-tool-guardrails)** —
  белый список на инструмент плюс хук, который отказывает опасной форме до запуска.
- **[Песочница без root](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/04-role-profiles)** —
  proot, одно дерево на запись, домашний каталог вообще не примонтирован.
- **[Сторож кошелька](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/01-agent-wallet-guard)** —
  лимиты и рубильник, который не зависит от собственного суждения агента.
- **[Публикация работы агента](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/03-agent-ops-playbook)** —
  стоп-лист, который срабатывает до `git push`: «я не забуду проверить» — это не контроль.

## 5. Доставка и внимание

- **[Голос, который приходит голосом](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/13-voice-input-hypotheses)** —
  аудио-ответ должен приходить голосовым сообщением и в темпе, который человек выдержит.
- **[Обязательства по доставке](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/28-digest-delivery-health)** —
  держите список того, что и когда должно быть доставлено, и проверяйте его, а не логи.
- **[Маршрутизация по темам](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/12-topic-routing)** —
  статус — в журнал, решения — человеку, а тревоги — туда, где их увидят.
- **[Тихие часы и частота](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/03-agent-ops-playbook)** —
  дайджест, который приходит, когда его не читают, приучает игнорировать дайджесты.

## 6. Память, которая не гниёт

- **[Память по темам](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/09-ops-as-data)** —
  маленькое ядро, всегда загруженное, плюс файл на каждую тему, читаемый по требованию.
- **[Гигиена сессий](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/08-session-housekeeping)** —
  сессия — это лог, а не картотека: назвать, заархивировать, подрезать.
- **[Уборщик библиотеки навыков](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/34-skill-library-janitor)** —
  навыки накапливаются, противоречат друг другу и описывают переименованные инструменты.
- **[Аудит слепых зон](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/21-blind-spot-audit)** —
  спросите, на что агент **не** смотрит; ответ обычно полезнее сводки.

## 7. Следить за машиной, а не только за моделью

- **[Супервизор шлюза](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/02-agent-gateway-supervisor)** —
  процесс, который говорит с мессенджером, — единственная точка отказа.
- **[Пробы стенда](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/18-harness-probes)** —
  синтетические проверки всего пути: модель, инструмент, транспорт, права.
- **[Операции как данные](https://github.com/ipanalytics/Hermes-Agent-Ops/tree/main/09-ops-as-data)** —
  каждая задача пишет строку; дашборд — это запрос, а не воспоминание.

## 8. Инструменты, которые стоит знать

- [**Hermes Agent**](https://hermes-agent.nousresearch.com/docs) — стенд, под который написан этот
  список: профили, кроны, навыки, плагины, инструмент терминала и мессенджер.
- [**proot**](https://proot-me.github.io/) — изоляция в пользовательском пространстве без root:
  так у терминала агента появляется рабочее дерево и больше ничего.
- [**edge-tts**](https://github.com/rany2/edge-tts) — бесплатный резервный голос, когда платный
  провайдер упёрся в лимит в 03:10.
- [**Jev (TypeSafe)**](https://github.com/kerpopule/hermes-jev-skills) — дешёвые решения
  (маршрутизация, выбор навыка, компакция) принимает маленькая быстрая модель, а не дорогая.
- [**RIPE RIS**](https://ris.ripe.net) — публичные дампы BGP RIB, сырьё для работы с
  безопасностью маршрутизации. [**CAIDA**](https://www.caida.org/catalog/datasets/) — связи между
  AS, [**MaxMind GeoLite2**](https://dev.maxmind.com/geoip/geolite2-free-geolocation-data) —
  географический слой.
- [**SQLite FTS5**](https://sqlite.org/fts5.html) — полнотекстовый поиск по своей же истории
  сессий: единственная причина, по которой прошлое агента вообще пригодно к использованию.

## Чем этот список не является

- Не про промпт-инжиниринг. Это другая задача и другой список.
- Не фреймворк. Почти всё здесь — запись в кроне, скрипт и JSON-файл.
- Не закончен. Каждый пункт появился потому, что что-то сломалось.

## Как помочь

Правки и дополнения приветствуются — особенно **режимы отказа**: симптом, причина, лечение.
Одна строка на пункт, живая ссылка, без маркетинга.

## Лицензия

MIT для списка и для связанных модулей, если в модуле не сказано иное.
