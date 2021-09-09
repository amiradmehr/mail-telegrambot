from helper import progressBar


class Templates:


        def __init__(self,num):
            self.num = num
            

        def get(self, prof=None, topic=None, paper=None, arb1=None, arb2=None, arb3=None):
                self.temp1 = f'''

<p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:8pt;"><span style="font-size: 12px; font-family: Verdana, Geneva, sans-serif; color: rgb(0, 0, 0); background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">Dear Dr. {prof},</span></p>
<p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:8pt;"><span style="font-size: 12px;"><span style="font-family: Verdana, Geneva, sans-serif;"><span style="color: rgb(0, 0, 0); background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">My name is Amir Mohammad Radmehr. I graduated with a B.Sc. degree in Electrical Engineering (Control) from the University of Tehran,&nbsp;</span><span style="color: rgb(0, 0, 0); background-color: transparent; font-weight: 400; font-style: italic; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">(</span><a href="https://www.usnews.com/education/best-global-universities/university-of-tehran-504903" style="text-decoration:none;"><span style="color: rgb(5, 99, 193); background-color: transparent; font-weight: 400; font-style: italic; font-variant: normal; text-decoration: underline; text-decoration-skip-ink: none; vertical-align: baseline; white-space: pre-wrap;">ranked 1st&nbsp;top university in Iran according to 2021 US</span><span style="color: rgb(5, 99, 193); background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: underline; text-decoration-skip-ink: none; vertical-align: baseline; white-space: pre-wrap;">&nbsp;</span><span style="color: rgb(5, 99, 193); background-color: transparent; font-weight: 400; font-style: italic; font-variant: normal; text-decoration: underline; text-decoration-skip-ink: none; vertical-align: baseline; white-space: pre-wrap;">news ranking</span></a><span style="color: rgb(0, 0, 0); background-color: transparent; font-weight: 400; font-style: italic; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">)&nbsp;</span><span style="color: rgb(0, 0, 0); background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">with a major GPA of 3.64. My</span><a href="https://amirradmehr.wixsite.com/work/thesis" style="text-decoration:none;" target="_self"><span style="color: rgb(0, 0, 0); background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">&nbsp;</span><span style="color: rgb(17, 85, 204); background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: underline; text-decoration-skip-ink: none; vertical-align: baseline; white-space: pre-wrap;">thesis</span></a><span style="color: rgb(17, 85, 204); background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: underline; text-decoration-skip-ink: none; vertical-align: baseline; white-space: pre-wrap;">&nbsp;</span><span style="color: rgb(0, 0, 0); background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">is about the imitation of human face angles using image processing methods and applies them to the Agile Eye 3DOF parallel robot and designing an animatronic eye mechanism.</span></span></span></p>
<p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:8pt;"><span style="font-size: 12px;"><span style="font-family: Verdana, Geneva, sans-serif;"><span style="color: rgb(0, 0, 0); background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">Your research on {topic} is really interesting for me. More specifically, your work on {paper}, which I think is aligned with my interests and background.</span></span></span></p>
<p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:8pt;"><span style="font-size: 12px;"><span style="font-family: Verdana, Geneva, sans-serif;"><span style="color: rgb(0, 0, 0); background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">I would like to pursue my education with a graduate degree under your supervision. Please let me know how I can proceed to apply for joining your team.</span></span></span></p>
<p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:8pt;"><span style="font-size: 12px;"><span style="font-family: Verdana, Geneva, sans-serif;"><span style="color: rgb(0, 0, 0); background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">For more information, I have attached my CV.</span></span></span></p>
<p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:8pt;"><span style="font-size: 12px;"><span style="font-family: Verdana, Geneva, sans-serif;"><span style="color: rgb(0, 0, 0); background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">Also, you can find more on my website:</span></span></span></p>
<p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:8pt;"><span style="font-size: 12px;"><span style="font-family: Verdana, Geneva, sans-serif;"><a href="https://amirradmehr.wixsite.com/work" style="text-decoration:none;"><span style="color: rgb(5, 99, 193); background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: underline; text-decoration-skip-ink: none; vertical-align: baseline; white-space: pre-wrap;">amirradmehr.wixsite.com/work</span></a></span></span></p>
<p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:8pt;"><span style="font-size: 12px;"><span style="font-family: Verdana, Geneva, sans-serif;"><span style="color: rgb(0, 0, 0); background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">Yours sincerely,</span></span></span></p>
<p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:8pt;"><span style="font-size: 12px; font-family: Verdana, Geneva, sans-serif; color: rgb(0, 0, 0); background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">Amir Mohammad Radmehr</span></p>'''
                self.temp2 = f'''

Hello {prof}
                
                '''

                temps = [self.temp1, self.temp2]

                return temps[self.num-1]

