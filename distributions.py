import numpy as np
from scipy.stats import norm
from scipy.stats import powernorm
from scipy.stats import lognorm
from scipy.stats import powerlognorm
from scipy.stats import laplace
from scipy.stats import laplace_asymmetric
from scipy.stats import expon
from scipy.stats import cauchy
from scipy.stats import skewcauchy
from scipy.stats import chi
from scipy.stats import chi2
from scipy.stats import t
from scipy.stats import f
from scipy.stats import gamma
from scipy.stats import exponweib
from scipy.stats import weibull_min
from scipy.stats import weibull_max
from scipy.stats import johnsonsu
from scipy.stats import genhyperbolic
from scipy.stats import genextreme
from scipy.stats import tukeylambda
np.warnings.filterwarnings("ignore", category=RuntimeWarning)


class Distributions():

    def normal_fit(self, data):
        x = np.linspace(data.min(), data.max(), num=len(data))
        params = norm.fit(data)
        llh = norm.logpdf(data, *params).sum()
        bic = self.bayesian_information_criterion(data, params, llh)
        aic = self.akaike_information_criterion(params, llh)
        pdf = norm.pdf(x, params[0], params[1])
        cdf = norm.cdf(x, params[0], params[1])
        return llh, bic, aic, x, pdf, cdf, params[-2], params[-1]

    def pnorm_fit(self, data):
        x = np.linspace(data.min(), data.max(), num=len(data))
        params = powernorm.fit(data)
        llh = powernorm.logpdf(data, *params).sum()
        bic = self.bayesian_information_criterion(data, params, llh)
        aic = self.akaike_information_criterion(params, llh)
        pdf = powernorm.pdf(x, params[0], params[1], params[2])
        cdf = powernorm.cdf(x, params[0], params[1], params[2])
        return llh, bic, aic, x, pdf, cdf, params[-2], params[-1]

    def lognormal_fit(self, data):
        x = np.linspace(data.min(), data.max(), num=len(data))
        params = lognorm.fit(data)
        llh = lognorm.logpdf(data, *params).sum()
        bic = self.bayesian_information_criterion(data, params, llh)
        aic = self.akaike_information_criterion(params, llh)
        pdf = lognorm.pdf(x, params[0], params[1], params[2])
        cdf = lognorm.cdf(x, params[0], params[1], params[2])
        return llh, bic, aic, x, pdf, cdf, params[-2], params[-1]

    def plognorm_fit(self, data):
        x = np.linspace(data.min(), data.max(), num=len(data))
        params = powerlognorm.fit(data)
        llh = powerlognorm.logpdf(data, *params).sum()
        bic = self.bayesian_information_criterion(data, params, llh)
        aic = self.akaike_information_criterion(params, llh)
        pdf = powerlognorm.pdf(x, params[0], params[1], params[2], params[3])
        cdf = powerlognorm.cdf(x, params[0], params[1], params[2], params[3])
        return llh, bic, aic, x, pdf, cdf, params[-2], params[-1]

    def expon_fit(self, data):
        x = np.linspace(data.min(), data.max(), num=len(data))
        params = expon.fit(data)
        llh = expon.logpdf(data, *params).sum()
        bic = self.bayesian_information_criterion(data, params, llh)
        aic = self.akaike_information_criterion(params, llh)
        pdf = expon.pdf(x, params[0], params[1])
        cdf = expon.cdf(x, params[0], params[1])
        return llh, bic, aic, x, pdf, cdf, params[-2], params[-1]

    def laplace_fit(self, data):
        x = np.linspace(data.min(), data.max(), num=len(data))
        params = laplace.fit(data)
        llh = laplace.logpdf(data, *params).sum()
        bic = self.bayesian_information_criterion(data, params, llh)
        aic = self.akaike_information_criterion(params, llh)
        pdf = laplace.pdf(x, params[0], params[1])
        cdf = laplace.cdf(x, params[0], params[1])
        return llh, bic, aic, x, pdf, cdf, params[-2], params[-1]

    def laplaceAsym_fit(self, data):
        x = np.linspace(data.min(), data.max(), num=len(data))
        params = laplace_asymmetric.fit(data)
        llh = laplace_asymmetric.logpdf(data, *params).sum()
        bic = self.bayesian_information_criterion(data, params, llh)
        aic = self.akaike_information_criterion(params, llh)
        pdf = laplace_asymmetric.pdf(x, params[0], params[1], params[2])
        cdf = laplace_asymmetric.cdf(x, params[0], params[1], params[2])
        return llh, bic, aic, x, pdf, cdf, params[-2], params[-1]

    def cauchy_fit(self, data):
        x = np.linspace(data.min(), data.max(), num=len(data))
        params = cauchy.fit(data)
        llh = cauchy.logpdf(data, *params).sum()
        bic = self.bayesian_information_criterion(data, params, llh)
        aic = self.akaike_information_criterion(params, llh)
        pdf = cauchy.pdf(x, params[0], params[1])
        cdf = cauchy.cdf(x, params[0], params[1])
        return llh, bic, aic, x, pdf, cdf, params[-2], params[-1]

    def skewcauchy_fit(self, data):
        x = np.linspace(data.min(), data.max(), num=len(data))
        params = skewcauchy.fit(data)
        llh = skewcauchy.logpdf(data, *params).sum()
        bic = self.bayesian_information_criterion(data, params, llh)
        aic = self.akaike_information_criterion(params, llh)
        pdf = skewcauchy.pdf(x, params[0], params[1])
        cdf = skewcauchy.cdf(x, params[0], params[1])
        return llh, bic, aic, x, pdf, cdf, params[-2], params[-1]

    def chi_fit(self, data):
        x = np.linspace(data.min(), data.max(), num=len(data))
        params = chi.fit(data)
        llh = chi.logpdf(data, *params).sum()
        bic = self.bayesian_information_criterion(data, params, llh)
        aic = self.akaike_information_criterion(params, llh)
        pdf = chi.pdf(x, params[0], params[1], params[2])
        cdf = chi.cdf(x, params[0], params[1], params[2])
        return llh, bic, aic, x, pdf, cdf, params[-2], params[-1]

    def chi2_fit(self, data):
        x = np.linspace(data.min(), data.max(), num=len(data))
        params = chi2.fit(data)
        llh = chi2.logpdf(data, *params).sum()
        bic = self.bayesian_information_criterion(data, params, llh)
        aic = self.akaike_information_criterion(params, llh)
        pdf = chi2.pdf(x, params[0], params[1], params[2])
        cdf = chi2.cdf(x, params[0], params[1], params[2])
        return llh, bic, aic, x, pdf, cdf, params[-2], params[-1]

    def tdist_fit(self, data):
        x = np.linspace(data.min(), data.max(), num=len(data))
        params = t.fit(data)
        llh = t.logpdf(data, *params).sum()
        bic = self.bayesian_information_criterion(data, params, llh)
        aic = self.akaike_information_criterion(params, llh)
        pdf = t.pdf(x, params[0], params[1], params[2])
        cdf = t.cdf(x, params[0], params[1], params[2])
        return llh, bic, aic, x, pdf, cdf, params[-2], params[-1]

    def fdist_fit(self, data):
        x = np.linspace(data.min(), data.max(), num=len(data))
        params = f.fit(data)
        llh = f.logpdf(data, *params).sum()
        bic = self.bayesian_information_criterion(data, params, llh)
        aic = self.akaike_information_criterion(params, llh)
        pdf = f.pdf(x, params[0], params[1], params[2], params[3])
        cdf = f.cdf(x, params[0], params[1], params[2], params[3])
        return llh, bic, aic, x, pdf, cdf, params[-2], params[-1]

    def gamma_fit(self, data):
        x = np.linspace(data.min(), data.max(), num=len(data))
        params = gamma.fit(data)
        llh = gamma.logpdf(data, *params).sum()
        bic = self.bayesian_information_criterion(data, params, llh)
        aic = self.akaike_information_criterion(params, llh)
        pdf = gamma.pdf(x, params[0], params[1], params[2])
        cdf = gamma.cdf(x, params[0], params[1], params[2])
        return llh, bic, aic, x, pdf, cdf, params[-2], params[-1]

    def weibullexpon_fit(self, data):
        x = np.linspace(data.min(), data.max(), num=len(data))
        params = exponweib.fit(data)
        llh = exponweib.logpdf(data, *params).sum()
        bic = self.bayesian_information_criterion(data, params, llh)
        aic = self.akaike_information_criterion(params, llh)
        pdf = exponweib.pdf(x, params[0], params[1], params[2], params[3])
        cdf = exponweib.cdf(x, params[0], params[1], params[2], params[3])
        return llh, bic, aic, x, pdf, cdf, params[-2], params[-1]

    def weibullmin_fit(self, data):
        x = np.linspace(data.min(), data.max(), num=len(data))
        params = weibull_min.fit(data)
        llh = weibull_min.logpdf(data, *params).sum()
        bic = self.bayesian_information_criterion(data, params, llh)
        aic = self.akaike_information_criterion(params, llh)
        pdf = weibull_min.pdf(x, params[0], params[1], params[2])
        cdf = weibull_min.cdf(x, params[0], params[1], params[2])
        return llh, bic, aic, x, pdf, cdf, params[-2], params[-1]

    def weibullmax_fit(self, data):
        x = np.linspace(data.min(), data.max(), num=len(data))
        params = weibull_max.fit(data)
        llh = weibull_max.logpdf(data, *params).sum()
        bic = self.bayesian_information_criterion(data, params, llh)
        aic = self.akaike_information_criterion(params, llh)
        pdf = weibull_max.pdf(x, params[0], params[1], params[2])
        cdf = weibull_max.cdf(x, params[0], params[1], params[2])
        return llh, bic, aic, x, pdf, cdf, params[-2], params[-1]

    def johnsonsu_fit(self, data):
        x = np.linspace(data.min(), data.max(), num=len(data))
        params = johnsonsu.fit(data)
        llh = johnsonsu.logpdf(data, *params).sum()
        bic = self.bayesian_information_criterion(data, params, llh)
        aic = self.akaike_information_criterion(params, llh)
        pdf = johnsonsu.pdf(x, params[0], params[1], params[2], params[2])
        cdf = johnsonsu.cdf(x, params[0], params[1], params[2], params[3])
        return llh, bic, aic, x, pdf, cdf, params[-2], params[-1]

    def genhyperbolic_fit(self, data):
        x = np.linspace(data.min(), data.max(), num=len(data))
        params = genhyperbolic.fit(data)
        llh = genhyperbolic.logpdf(data, *params).sum()
        bic = self.bayesian_information_criterion(data, params, llh)
        aic = self.akaike_information_criterion(params, llh)
        pdf = genhyperbolic.pdf(
            x, params[0], params[1], params[2], params[3], params[4])
        cdf = genhyperbolic.cdf(
            x, params[0], params[1], params[2], params[3], params[4])
        return llh, bic, aic, x, pdf, cdf, params[-2], params[-1]

    def genextreme_fit(self, data):
        x = np.linspace(data.min(), data.max(), num=len(data))
        params = genextreme.fit(data)
        llh = genextreme.logpdf(data, *params).sum()
        bic = self.bayesian_information_criterion(data, params, llh)
        aic = self.akaike_information_criterion(params, llh)
        pdf = genextreme.pdf(x, params[0], params[1], params[2])
        cdf = genextreme.cdf(x, params[0], params[1], params[2])
        return llh, bic, aic, x, pdf, cdf, params[-2], params[-1]

    def turklamda_fit(self, data):
        x = np.linspace(data.min(), data.max(), num=len(data))
        params = tukeylambda.fit(data)
        llh = tukeylambda.logpdf(data, *params).sum()
        bic = self.bayesian_information_criterion(data, params, llh)
        aic = self.akaike_information_criterion(params, llh)
        pdf = tukeylambda.pdf(x, params[0], params[1], params[2])
        cdf = tukeylambda.cdf(x, params[0], params[1], params[2])
        return llh, bic, aic, x, pdf, cdf, params[-2], params[-1]

    def bayesian_information_criterion(self, data, params, llh):
        bic = len(params)*np.log(len(data)) - 2*np.log(llh)
        return bic

    def akaike_information_criterion(self, params, llh):
        aic = 2*len(params) - 2*np.log(llh)
        return aic
