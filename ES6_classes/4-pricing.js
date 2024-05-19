import Currency from './3-currency'

export default class Pricing {
  constructor(amount, currency) {
    this._amount = amount;
    this._currency = currency;
  }

  get amount() {
    return this._amount;
  }

  get currency() {
    return this._currency;
  }

  set amount(newamount) {
    if (typeof newamount === 'number') {
      this._amount = newamount;
    }
  }

  set currency(newcurr) {
    if (newcurr instanceof Currency) {
      this._currency = newcurr;
    }
  }

  displayFullPrice() {
    return `${this.amount} ${this.currency.name} (${this.currency.code})`;
  }

  static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }
}
