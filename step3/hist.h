#ifndef HIST_H
#define HIST_H

#include <QWidget>

namespace Ui {
class Hist;
}

class Hist : public QWidget
{
    Q_OBJECT

public:
    explicit Hist(QWidget *parent = 0);
    ~Hist();

private:
    Ui::Hist *ui;
};

#endif // HIST_H
