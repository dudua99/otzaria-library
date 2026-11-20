NOT READY

# סיכום

הבנייה המלאה (v1 + v2), הדחיסה והפטש עברו, ו-`producePatchAndVerify` אימת prev + patch == new. כל שורה בפטש שייכת לספרי שלושת התיקונים, ושום דבר אחר לא השתנה (ספירות book/line/link/line_note/author/category זהות ב-v1 וב-v2).

**#2766 ו-#3468 מוכנים.** **#3775 תיקן רק חצי**: ב«מאמר דבר תורה» כל 39 ההערות קיבלו סימן (hasMarker 0→39). ב«חידושי הריטבא סוכה מכתב יד» כל 19 ההערות נשארו hasMarker=0, ולכן הכרעה: NOT READY.

# לפי תיקון

## #2766 — `fix/dicta-gershayim-2766` @ 1636e1b (קומיט אחד על upstream main 0e95a92)
- מאמתים: עוברים (פירוט למטה).
- פטש: `upsert_book` ×3 (8037/8045/8061: title + heRef `עהת`→`עה״ת`) ו-`upsert_line` ×2312 (heRef בלבד: 8045×1604, 8037×509, 8061×199). נבדק שבכל 2312 השורות השתנה רק heRef, ו-lineIndex/tocEntryId/charCount זהים.
- U+05F4 (״) הוא הצורה ש-26 שמות קבצים נארזים אחרים כבר משתמשים בה. ב-DB ה-title שומר אותה, וזה אומת ב-v2.

## #3468 — `fix/pnei-hamelech-author-3468` @ 8deb2ca
- מאמתים: עוברים.
- פטש: `delete_author` 642 «רבי זקן משה מאגו'ז» (שימש רק את 6147) ו-`upsert_author` 1183 «רבי משה זקן מאזוז». `book_author` 6147: 642→1183. שורה 2 בספר (lineIndex 1) הוחלפה: delete/upsert של line, line_content ו-line_toc ×1, עם הטקסט החדש. `upsert_book` 6147: contentHash בלבד.

## #3775 — `fix/hearot-note-markers-3775` @ 131bd8d
- מאמתים: עוברים. טקסט ההערות ומספר השורות זהים (41/41, 21/21), ו-39+19 השורות תואמות ל-`NOTE_SMALL_SUP`. בכל הספרייה אין קובץ אחר עם `<sup><small>N</sup>`.
- 6726 «מאמר דבר תורה»: 39/39 הערות hasMarker=1, ו-charPos נמצא על הסימן. ב-21 שורות הבסיס `<sup>N</sup>` הפך ל-`<sup class="footnote-marker">N</sup>`. ✅
- 7952 «חידושי הריטבא סוכה מכתב יד»: **0/19**. ❌ הסיבה: בקובץ ההערות הסימן הוא `<small><sup>1)</sup> …</small>` (המספר עם סוגר `)`), ובספר הבסיס הסימן הוא `<sup>1</sup>`. `parseLeadingMarker` כבר מפרש את הדקדוק (התיקון הזה כן עבד), אבל `findAnchor` מחפש `<sup>1)</sup>`, לא מוצא, וההערה מצורפת בסוף השורה בלי סימן. זה נכון לכל 19 ההערות (1),6)…28)). ספר הבסיס מכיל `<sup>1</sup>`…`<sup>28</sup>`.
- מה שהפטש מראה ל-7952: 19 שורות קיבלו מזהה חדש עם טקסט זהה, 19 קישורי סוכה(108)→7952 מצביעים מחדש על המזהים החדשים (כל 85 הקישורים זהים עד כדי מזהה שורה), ו-19 line_note השתנו בגוף בלבד, עדיין hasMarker=0.
- **דורש הכרעה, לא תוקן**: (א) להסיר את ה-`)` מ-19 הסימנים בקובץ ההערות, כך שהסימן יהיה `<small><sup>1</sup> …`. זה משנה את טקסט הסימן המוצג (1) ל-1, כמו בספר הבסיס), ולכן אינו רק סדר תגים. (ב) או ללמד את `HearotCompanionMerge` להתאים `N)` להערה ל-`<sup>N</sup>` בבסיס. ההוראות אסרו ליצור את הענפים מחדש, להוסיף להם קומיט שני או לדחוף בכוח, ולכן הענף נשאר כפי שהוא.

# בלתי-צפוי / הערות
- **מזהי הספרים שבהוראות (7849/7852/7862, 7201, 6096/6890) אינם המזהים בבנייה זו.** v1 נבנה ממקצה ריק, כמו `delta-real-diff-test.yml` (שאינו זורע את buildstate של השחרור), ולכן המזהים שונים. בבנייה זו 7849 הוא «שלמי כהן יבמות», 7201 «שות מהרם בן חביב», 6096 «מכתם לדוד», 6890 «אבני נזר חושן משפט», ואף אחד מהם לא הופיע בפטש. ההתאמה נעשתה לפי שם: 8037/8045/8061, 6147, 6726/7952.
- ספר 108 (סוכה) מופיע רק בצד המקור של 19 קישורי 7952 (הוסבר למעלה).
- שורות שתוכנן השתנה מקבלות מזהה שורה חדש (delete+upsert) במקום עדכון במקום. זו התנהגות המקצה, והיא חלה גם על שורות 7952 שהטקסט שלהן זהה, כי שורת המקור הגולמית (עם ההערה המצורפת) השתנתה.

# מאמתים (על כל ענף, מול origin/main 0e95a92)
| בדיקה | 2766 | 3468 | 3775 | main |
|---|---|---|---|---|
| check_author_mirrors.py --base origin/main | ✅ | ✅ | ✅ | |
| validate_fordb_book_names.py --rename-base origin/main * | ✅ | ✅ | ✅ | ✅ |
| check_locked_metadata.py --git-rev HEAD --since origin/main | ✅ | ✅ | ✅ | |
| check_locked_metadata.py (מלא, עץ עבודה) | ✅ | ✅ | ✅ | |
| fordb_archive.py build | ✅ | ✅ | ✅ | |
| split_long_lines.py --check-changed origin/main | ✅ | ✅ | ✅ | |
| unittest של validate-fordb-book-names.yml (196 בדיקות) | ✅ | ✅ | ✅ | |
| post_convert_fixes.py --check National-LibraryToOtzaria | ✅ | ✅ | ✅ | |
| post_convert_fixes.py --check DictaToOtzaria ** | 6 בעיות | 6 | 6 | 6 (זהה) |

\* sefaria.org חסום כאן. עם SEFARIA_FETCH=0 נכשל באופן זהה גם על main (575 שמות חסרים). הורץ עם SEFARIA_FETCH=1, כשהתשובה של `/api/index/` מוגשת מ-`table_of_contents.json` של יצוא ספריא של v38 (`run_names_offline.py`). כך עובר על כל הענפים ועל main. ב-2766 הוא מדווח על 3 שינויי שם «איות בלבד» שכבר מיושרים.
\** אותן 6 בעיות בדיוק גם על main (שורות 1572, 1775, 2010, 2028, 2214, 2215). קיימות מראש, לא נגרמו על ידי התיקונים.
לא הורצו (דורשים רשת/נכסים חסומים): validate-sefaria-shadowed-books, validate-author-biographies, validate-manual-links-refs (התיקונים אינם נוגעים בקישורים).

# הבנייה
- קלטים מ-`build_provenance.json` של `v38-20261112163847`: sefaria `2026-11-12_17-17-43245592963-1` (sha f9b489b5… ✓), otzaria `library-links-43257538957-1-1917c47c4707` (sha f1601f39… ✓), fordb `50cf9d07…` (✓). SeforimLibrary @ da12467770a4.
- v2: אותם קלטים, והתיקונים הוחלו בנתיבים הנארזים (`אוצריא/…`) לפי `BOOK_ROOTS`: 3 שינויי שם, 3 קובצי ספר, `metadata.json`, `אודות התוכנה/SourcesBooks.csv` ו-`files_manifest.json` (מפתחות שם חדשים + sha256 מחושב מחדש, כמו ש-update-library מייצר). ForDB: all_metadata.json, book_info.csv ו-sefaria_metadata_changes.csv. ארכיון חדש `166c758c…` נבנה ב-`fordb_archive.build` בלי בדיקת הכיסוי, כי ForDB של v38 קודם ל-gemara_daf_alt_toc/inline_marker_alt_toc. אותה בנייה על ForDB של v38 מחזירה בדיוק `50cf9d07…`. v2 נזרע מ-buildstate של v1.
- זמנים: v1 18240s (5:04), v2 18432s (5:07), compress v1 1409s, compress v2 1343s, producePatchAndVerify 529s.
- מכונה: 4 ליבות, 15GB RAM, אין swap. generatorHeap=10g, inMemoryDb=false (מבוסס קובץ). DB לא דחוס 9.7GB. דיסק: לכל היותר כ-51GB בשימוש.
- תמונות ספריא: textimages.sefaria.org חסום, ותמונות שאינן ביצוא נשארו כ-URL. כשל זהה ב-v1 וב-v2, ולכן לא נכנס לפטש.
- acronymizer.db: Otzaria/SeforimAcronymizer `20261111.56` (האחרון לפני בניית v38). lexical.db לא הורד (`-x :packaging:downloadLexicalDb`), כי אינו חלק מ-seforim.db.

# עקיפות מקומיות (לא נכנסו לשום קומיט)
ראו `local_workarounds.diff` (מצורף בענף זה).
