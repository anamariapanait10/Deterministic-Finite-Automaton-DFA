
g = open("data.out", "w")


def read_data():
    number_of_states = None
    number_of_transitions = None
    transitions = {}
    initial_state = None
    final_states = []
    number_of_words = None
    words = []

    with open("data.in") as f:
        line_1 = f.readline().split()
        number_of_states = int(line_1[0])
        number_of_transitions = int(line_1[1])

        for i in range(number_of_transitions):
            line_i = f.readline().split()
            line_i[0] = int(line_i[0])
            line_i[1] = int(line_i[1])

            if line_i[0] in transitions:
                transitions[line_i[0]][line_i[2]] = line_i[1]
            else:
                transitions[line_i[0]] = {line_i[2]: line_i[1]}

        line = f.readline().split()
        initial_state = int(line[0])
        line = f.readline().split()
        final_states = [int(x) for x in line[1:]]
        line = f.readline().split()
        number_of_words = int(line[0])

        for i in range(number_of_words):
            line = f.readline().split()
            words.append(line[0])

    check_words(transitions, initial_state, final_states, words)


def check_words(transitions, initial_state, final_states, words):
    for word in words:
        check_dfa(word, transitions, initial_state, final_states)
    g.close()


def check_dfa(word, transitions, initial_state, final_states):
    word_len = len(word)
    index = 0
    current_state = initial_state
    route = [str(initial_state)]

    while index < word_len:
        if word[index] in transitions[current_state]:
            current_state = transitions[current_state][word[index]]
            route.append(str(current_state))
        else:
            g.write("NO\n")
            break
        index += 1
    else:
        if current_state in final_states:
            g.write("YES\nRoute: ")
            g.write(" ".join(route) + "\n")
        else:
            g.write("NO\n")


if __name__ == '__main__':
    read_data()

