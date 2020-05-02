class Verb:
    def __init__(self, present_simple, past_simple, past_participle, russian):
        self.present_simple, self.present_simple_transcription = present_simple.split(' ', 1)
        self.past_simple, self.past_simple_transcription = past_simple.split(' ', 1)
        self.past_participle, self.past_participle_transcription = past_participle.split(' ', 1)
        self.russian = russian
    
    def __str__(self):
        return "{0} {1} {2} {3}".format(
            self.present_simple, 
            self.past_simple, 
            self.past_participle, 
            self.russian
        )
        
    def tenses(self):
        return {
            "Present simple" : self.present_simple,
            "Past simple" : self.past_simple,
            "Past participle" : self.past_participle
        }
    
    def tenses_transcription(self):
        return {
            "Present simple" : self.present_simple_transcription,
            "Past simple" : self.past_simple_transcription,
            "Past participle" : self.past_participle_transcription
        }
    
verbs = [
    Verb("become [bɪˈkʌm]", "became [bɪˈkeɪm]", "become [bɪˈkʌm]", "становиться"),
    Verb("begin [bɪˈgɪn]", "began [bɪˈgæn]", "begun [bɪˈgʌn]", "начинать"),
    Verb("break [breɪk]", "broke [broʊk]", "broken [broʊkən]", "ломать(ся)"),
    Verb("bring [brɪŋ]", "brought [brɔ:t]", "brought [brɔ:t]", "приносить"),
    Verb("build [bɪld]", "built [bɪlt]", "built [bɪlt]", "строить"),
    Verb("buy [baɪ]", "bought [bɔ:t]", "bought [bɔ:t]", "покупать"),
    Verb("choose [tʃu:z]", "chose [tʃoʊz]", "chosen [tʃoʊzn]", "выбирать"),
    Verb("come [kʌm]", "came [keɪm]", "come [kʌm]", "приходить"),
    Verb("cut [kʌt]", "cut [kʌt]", "cut [kʌt]", "резать"),
    Verb("do [du:]", "did [dɪd]", "done [dʌn]", "делать"),
    Verb("draw [drɔ:]", "drew [dru:]", "drawn [drɔ:n]", "рисовать"),
    Verb("drive [draɪv]", "drove [droʊv]", "driven [drɪvn]", "вести машину"),
    Verb("fall [fɔ:l]", "fell [fɛl]", "fallen [fɔ:lən]", "падать"),
    Verb("feel [fi:l]", "felt [fɛlt]", "felt [fɛlt]", "чувствовать"),
    Verb("find [faɪnd]", "found [faʊnd]", "found [faʊnd]", "находить"),
    Verb("get [get]", "got [gɒt]", "gotten/got [gɒtn/gɒt]", "получать"),
    Verb("give [gɪv]", "gave [geɪv]", "given [gɪvn]", "давать"),
    Verb("go [goʊ]", "went [wɛnt]", "gone [ɡɒn]", "идти"),
    Verb("grow [groʊ]", "grew [gru:]", "grown [groʊn]", "расти"),
    Verb("have [hæv]", "had [hæd]", "had [hæd]", "иметь"),
    Verb("hear [hɪə]", "heard [hɜ:d]", "heard [hɜ:d]", "слышать"),
    Verb("hold [hoʊld]", "held [hɛld]", "held [hɛld]", "держать"),
    Verb("keep [ki:p]", "kept [kɛpt]", "kept [kɛpt]", "хранить"),
    Verb("know [noʊ]", "knew [nju:]", "known [noʊn]", "знать"),
    Verb("leave [li:v]", "left [lɛft]", "left [lɛft]", "оставлять"),
    Verb("let [lɛt]", "let [lɛt]", "let [lɛt]", "позволять"),
    Verb("lie [laɪ]", "lay [leɪ]", "lain [leɪn]", "лежать"),
    Verb("lose [lu:z]", "lost [lɒst]", "lost [lɒst]", "терять"),
    Verb("make [meɪk]", "made [meɪd]", "made [meɪd]", "делать (изготавливать)"),
    Verb("mean [mi:n]", "meant [mɛnt]", "meant [mɛnt]", "означать"),
    Verb("meet [mi:t]", "met [mɛt]", "met [mɛt]", "встречать"),
    Verb("pay [peɪ]", "paid [peɪd]", "paid [peɪd]", "платить"),
    Verb("put [pʊt]", "put [pʊt]", "put [pʊt]", "класть"),
    Verb("read [ri:d]", "read [rɛd]", "read [rɛd]", "читать"),
    Verb("rise [raɪz]", "rose [roʊz]", "risen [rɪzn]", "поднимать(ся)"),
    Verb("run [rʌn]", "ran [ræn]", "run [rʌn]", "бежать"),
    Verb("say [sɛɪ]", "said [sɛd]", "said [sɛd]", "говорить"),
    Verb("see [si:]", "saw [sɔ:]", "seen [si:n]", "видеть"),
    Verb("send [sɛnd]", "sent [sɛnt]", "sent [sɛnt]", "посылать"),
    Verb("set [sɛt]", "set [sɛt]", "set [sɛt]", "устанавливать"),
    Verb("show [ʃoʊ]", "showed [ʃoʊd]", "shown [ʃoʊn]", "показывать"),
    Verb("sit [sɪt]", "sat [sæt]", "sat [sæt]", "сидеть"),
    Verb("speak [spi:k]", "spoke [spoʊk]", "spoken [spoʊkən]", "разговаривать"),
    Verb("spend [spend]", "spent [spɛnt]", "spent [spɛnt]", "тратить, проводить (время)"),
    Verb("stand [stænd]", "stood [stʊd]", "stood [stʊd]", "стоять"),
    Verb("take [teɪk]", "took [tʊk]", "taken ['teɪkən]", "брать"),
    Verb("tell [tel]", "told [toʊld]", "told [toʊld]", "рассказывать"),
    Verb("think [θɪŋk]", "thought [θɔ:t]", "thought [θɔ:t]", "думать"),
    Verb("wear [wɛə]", "wore [wɔ:]", "worn [wɔ:n]", "надевать"),
    Verb("write [raɪt]", "wrote [roʊt]", "written [rɪtn]", "писать")
]

import random

greeting = """Enter the requested form for the verb.
Supported teams:
    '!' - show statistics and exit
    '?' - skip / show correct answer"""
print(greeting)

statistics = {"passed":0, "failed":0}

while True:
    selected = random.randint(0, len(verbs) - 1)
    verb = verbs[selected]
    tenses = verb.tenses()
    tenses_keys = list(tenses.keys())
    tense_to_show = random.choice(tenses_keys)
    tense_to_ask = random.choice(tenses_keys)
    tenses_transcription = verb.tenses_transcription()

    question = "{VERB} {TRANSCRIPTION} - {RUSSIAN}\n{FORM}:".format(
        FORM=tense_to_ask,
        VERB=tenses[tense_to_show], 
        TRANSCRIPTION=tenses_transcription[tense_to_show], 
        RUSSIAN=verb.russian
    )

    answer = input(question)
    if answer == "!":
        answers = statistics["passed"] + statistics["failed"]
        pass_rate = 0
        if answers > 0:
            pass_rate = statistics["passed"] / answers * 100
        statistics_format_string = "{PASS_RATE:.2f}% your answers were correct, only {PASSED} was correct and {FAILED} wrong."
        print(statistics_format_string.format(
            PASS_RATE=pass_rate, 
            PASSED=statistics["passed"], 
            FAILED=statistics["failed"])
        )
        input("Press Enter to end the script.")
        break
    elif answer == "?":
        statistics["failed"] += 1
        print(tenses[tense_to_ask])
    elif(answer == tenses[tense_to_ask]):
        statistics["passed"] += 1
        print("Right")
    else:
        statistics["failed"] += 1
        print("Wrong")

