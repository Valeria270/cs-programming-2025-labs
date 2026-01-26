reports = [
    {"author": "Dr. Moss", "text": "Analysis completed. Reference: http://external-archive.net"},
    {"author": "Agent Lee", "text": "Incident resolved without escalation."},
    {"author": "Dr. Patel", "text": "Supplementary data available at https://secure-research.org"},
    {"author": "Supervisor Kane", "text": "No anomalies detected during inspection."},
    {"author": "Researcher Bloom", "text": "Extended observations uploaded to http://research-notes.lab"},
    {"author": "Agent Novak", "text": "Perimeter secured. No external interference observed."},
    {"author": "Dr. Hargreeve", "text": "Full containment log stored at https://internal-db.scp"},
    {"author": "Technician Moore", "text": "Routine maintenance completed successfully."},
    {"author": "Dr. Alvarez", "text": "Cross-reference materials: http://crosslink.foundation"},
    {"author": "Security Officer Tan", "text": "Shift completed without incidents."},
    {"author": "Analyst Wright", "text": "Statistical model published at https://analysis-hub.org"},
    {"author": "Dr. Kowalski", "text": "Behavioral deviations documented internally."},
    {"author": "Agent Fischer", "text": "Additional footage archived: http://video-storage.sec"},
    {"author": "Senior Researcher Hall", "text": "All test results verified and approved."},
    {"author": "Operations Lead Grant", "text": "Emergency protocol draft shared via https://ops-share.scp"}
]
import re
reports_with_links = list(filter(lambda report: 'http' in report['text'], reports))
print("Отчеты с внешними ссылками:")
for report in reports_with_links:
    print(f"Автор: {report['author']}")
    print(f"Текст: {report['text']}")
    print("-" * 50)
cleaned_reports = list(map(
    lambda report: {
        "author": report["author"],
        "text": re.sub(r'https?://[^\s]+', '[ДАННЫЕ УДАЛЕНЫ]', report["text"])
    },
    reports_with_links
))

print("\n" + "="*50)
print("Очищенные отчеты:")
print("="*50)

for report in cleaned_reports:
    print(f"Автор: {report['author']}")
    print(f"Текст: {report['text']}")
    print("-" * 50)