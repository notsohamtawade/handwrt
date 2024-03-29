
import os
import itertools
import sklearn
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import extract
import categorize

X_baseline_angle = []
X_top_margin = []
X_letter_size = []
X_line_spacing = []
X_word_spacing = []
X_pen_pressure = []
X_slant_angle = []
y_t1 = []
y_t2 = []
y_t3 = []
y_t4 = []
y_t5 = []
y_t6 = []
y_t7 = []
y_t8 = []
page_ids = []

if os.path.isfile("label_list.txt"):
    print("Info: label_list found.")
    # =================================================================
    with open("label_list.txt", "r") as labels:
        for line in labels:
            content = line.split()

            baseline_angle = float(content[0])
            X_baseline_angle.append(baseline_angle)

            top_margin = float(content[1])
            X_top_margin.append(top_margin)

            letter_size = float(content[2])
            X_letter_size.append(letter_size)

            line_spacing = float(content[3])
            X_line_spacing.append(line_spacing)

            word_spacing = float(content[4])
            X_word_spacing.append(word_spacing)

            pen_pressure = float(content[5])
            X_pen_pressure.append(pen_pressure)

            slant_angle = float(content[6])
            X_slant_angle.append(slant_angle)

            trait_1 = float(content[7])
            y_t1.append(trait_1)

            trait_2 = float(content[8])
            y_t2.append(trait_2)

            trait_3 = float(content[9])
            y_t3.append(trait_3)

            trait_4 = float(content[10])
            y_t4.append(trait_4)

            trait_5 = float(content[11])
            y_t5.append(trait_5)

            trait_6 = float(content[12])
            y_t6.append(trait_6)

            trait_7 = float(content[13])
            y_t7.append(trait_7)

            trait_8 = float(content[14])
            y_t8.append(trait_8)

            page_id = content[15]
            page_ids.append(page_id)
    # ===============================================================

    # emotional stability
    X_t1 = []
    for a, b in zip(X_baseline_angle, X_slant_angle):
        X_t1.append([a, b])

    # mental energy or will power
    X_t2 = []
    for a, b in zip(X_letter_size, X_pen_pressure):
        X_t2.append([a, b])

    # modesty
    X_t3 = []
    for a, b in zip(X_letter_size, X_top_margin):
        X_t3.append([a, b])

    # personal harmony and flexibility
    X_t4 = []
    for a, b in zip(X_line_spacing, X_word_spacing):
        X_t4.append([a, b])

    # lack of discipline
    X_t5 = []
    for a, b in zip(X_slant_angle, X_top_margin):
        X_t5.append([a, b])

    # poor concentration
    X_t6 = []
    for a, b in zip(X_letter_size, X_line_spacing):
        X_t6.append([a, b])

    # non communicativeness
    X_t7 = []
    for a, b in zip(X_letter_size, X_word_spacing):
        X_t7.append([a, b])

    # social isolation
    X_t8 = []
    for a, b in zip(X_line_spacing, X_word_spacing):
        X_t8.append([a, b])

    # print X_t1
    # print type(X_t1)
    # print len(X_t1)

    X_train, X_test, y_train, y_test = train_test_split(
        X_t1, y_t1, test_size=.30, random_state=8)
    clf1 = SVC(kernel='rbf')
    clf1.fit(X_train, y_train)
    print("Classifier 1 accuracy: ", accuracy_score(
        clf1.predict(X_test), y_test))

    X_train, X_test, y_train, y_test = train_test_split(
        X_t2, y_t2, test_size=.30, random_state=16)
    clf2 = SVC(kernel='rbf')
    clf2.fit(X_train, y_train)
    print("Classifier 2 accuracy: ", accuracy_score(
        clf2.predict(X_test), y_test))

    X_train, X_test, y_train, y_test = train_test_split(
        X_t3, y_t3, test_size=.30, random_state=32)
    clf3 = SVC(kernel='rbf')
    clf3.fit(X_train, y_train)
    print("Classifier 3 accuracy: ", accuracy_score(
        clf3.predict(X_test), y_test))

    