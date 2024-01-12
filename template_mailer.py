
email_template=[
{"text": """Hi [name]

Thank you so much for [action they did] It was such a pleasure to work with you, and I'm very excited about the next opportunity to work together again.

Please don't hesitate to contact me if I can provide any additional information.

Best regards,

[name and job title]""", "label":"Thankyou"},


{"text": """Dear [name of hiring manager],

I enjoyed speaking with you the other day at the interview for the [job name]. The job appears to be an ideal match for my skills, ambitions, and interests.

The innovative approach to the corporate culture within the [job field] world confirmed my wish to work at your firm.

I will bring my engineering skills, assertiveness, and ability to engage others to work in a cooperative way within the [name of department] department.

Thank you for taking the time to interview me for the [position title] at [company]. I have a high level of interest in working for your firm and look forward to hearing from you.

Best Regards,

[name]""", "label":"Thankyou1"},


{"text": """Dear Mr./Mrs. [name],

I would like to formally recognize all the hard work and dedication you've put into completing [project/task]. Due to your consistent efforts, the project is what it is today and that led to the positive results we were hoping for. 

On behalf of [company name, board members, etc.], we would like to formally thank you for your hard work and we would like to let you know that we highly value your contribution and your continued dedication to your job.

We are very grateful to have you as a member of our team and we wish to continue to see you thrive within our organization.

Best regards,

[Name and job title]""", "label":"Thankyou2"},


{"text": """Dear [name],

On January 30th, 2020, I made a reservation at your restaurant located at 1234 Mulberry Lane for a birthday dinner for four people. This letter is intended to bring certain issues to your attention.

Unfortunately, we did not enjoy our dinner due to the fact that the food was very slow to arrive and we received the wrong dishes. It's understandable that it was a busy time at your restaurant, but the quality of the service was not as expected.

To resolve this problem, I would appreciate it if you could provide compensation in the form of a gift voucher or discount on a future meal. 

I'm looking forward to your reply.

With regards,

[Your name]""", "label":"Complaint"}

]


email_servers=[
    {"Name":"GMail(Google)", "server":"smtp.gmail.com","port":587},
    {"Name":"Yahoo", "server":"smtp.mail.yahoo.com","port":465},
    {"Name":"Hotmail", "server":"smtp.live.com","port":465},
    {"Name":"Outlook", "server":"smtp.office365.com","port":587},
]


