#include "hist.h"
#include "ui_hist.h"

Hist::Hist(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Hist)
{
    ui->setupUi(this);
}

Hist::~Hist()
{
    delete ui;
}
